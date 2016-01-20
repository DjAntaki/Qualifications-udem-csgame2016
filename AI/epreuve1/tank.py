# -*- coding: utf-8 -*- 

#Disclaimer : Désolé le code est un peu moche. Ça a pris plus de temps prévu à coder et ça a été écrit rapidement vers la fin.

import random
import re
from itertools import product
from copy import deepcopy

reg_valid = re.compile('NOPE|MINE|(MOVE\ |SHOOT\ )(UP|DOWN|LEFT|RIGHT)')

    

class GameManager:
    class GameConfig:
        def __init__(self, nb_player, max_mines, initial_life, iteration_limit):
            self.nb_players = nb_player
            self.max_mines = max_mines
            self.iteration_limit = iteration_limit
            self.initial_life = initial_life

    def __init__(self, players, battlefield, initial_life=50, max_mine=3, iteration_limit=200, random_start=False, display=True):
        """
        players : a list of decision functions. Each one will be 
        battlefield : a Map object instance
        initial_life : the initial number of lifes of each tank
        max_mines : the maximum number of mines that can drop a tank
        random_start : shuffle starting positions between players
        display : prints beautified game map state, decisions maded by players and damage dealt.
        
        """
        self.ginfo = self.GameConfig(len(players),max_mine, initial_life, iteration_limit)
        self.decision_functions = players   
        self.map=battlefield
        self.display = display
        if len(battlefield.initial_pos) > self.ginfo.nb_players:
            print("Too many players for the map")
        self.random_start = random_start

    def reset(self):
        """reinitialise game to initial state, places players at starting positions"""

        #Giving a random starting position to each players
        if self.random_start == True :
            positions = random.sample(self.map.initial_pos, nb_players)
        else :
            positions = self.map.initial_pos
        
        self.players = []
                    
        for i in range(self.ginfo.nb_players): 
            assert self.map.walls[positions[i][0]][positions[i][1]] == 0 #If this assertion fail then it means the map has a wall at a starting position
            self.players.append(Player(i, positions[i], self.ginfo.initial_life,self.ginfo.max_mines))        
        
        self.bullets = []
        self.mines = []
        self.players_alive = set(range(self.ginfo.nb_players))
        self.state = self.create_map_view(True,True)
        self.ginfo.counter = 0

    def create_map_view(self,player_id=False,mines=False):
        """  
        if player_id is true then player will be identified by the label "/id" where id is the integer number assigned to them at initialisation. 
        if player_id is False then all players will be identified by 'x'
        if mines is True then 'm' is placed on the map at its position.       
        
         """
        battlefield = [['' for i in range(self.map.shape[1])] for j in range(self.map.shape[0])]
        
        for i,j in product(range(self.map.shape[0]), range(self.map.shape[1])):
            if self.map.walls[i][j] :
                battlefield[i][j] = '|'
                
        if player_id :
            for p in self.players:
                battlefield[p.pos[0]][p.pos[1]] = p.label                    
        else :
            for p in self.players:
                battlefield[p.pos[0]][p.pos[1]] = 'x'            

        for b in self.bullets:
            battlefield[b.pos[0]][b.pos[1]] += "*"
            
        if mines :
            for m in self.mines:
                battlefield[m.pos[0]][m.pos[1]] += "m"    
            
        return battlefield
        
    def apply_filter(self,battlefield,mask,previous_explore):
        """apply mask (output of limited_view_mask function) in-place on battlefield"""
        for i,j in product(range(self.map.shape[0]),range(self.map.shape[1])):
            if not mask[i][j] :
                if previous_explore[i][j] :
                    if battlefield[i][j] != '|':
                        battlefield[i][j] = ','
                else :
                    battlefield[i][j] = '?'
            elif not previous_explore[i][j] :
                previous_explore[i][j] = True
            
        return battlefield
        
    def limited_view_mask(self, position, view_dist=10):
        """This function returns a 2d boolean matrix where element at index i,j is True if it could be seen by a player at position given in input.

        position : a tuple of 2 integers indicating the position of the player


        """

        mask = [[False for i in range(self.map.shape[1])] for j in range(self.map.shape[0])]
        p0, p1 = position
        mask[p0][p1] = True
        #Vue orthogonale
        for d0,d1 in (1,0),(-1,0),(0,1),(0,-1): # 2 orthogonal axis
            x,y = p0,p1
            for i in range(view_dist):
                x += d0
                y += d1
                if not self.position_on_board(x,y):
                    break
                mask[x][y] = True
                if self.map.walls[x][y]:
                    break

        
        #Vues diagonales                
        for d0,d1 in product([-1,1],repeat=2): #Four quadrants
            a = [(p0+d0*(i+1),p1+d1*(view_dist-i-1)) for i in range(view_dist-1)]

            for y0,y1 in a:
            # Shamelessly taken from https://en.wikipedia.org/wiki/Bresenham's_line_algorithm
                dx = y0-p0
                dy = y1-p1
                D = 2*dy - dx
                y = p1
                if D>0:
                    y = y+1
                    D = D - (2*dx)
                for x in range(p0+1,y1):
                    if not self.position_on_board(x,y):
                        break
                    mask[x][y] = True
                    if self.map.walls[x][y]:
                        break
                    D = D + (2*dx)
                    if D>0:
                        y = y+1
                        D = D - (2*dx)
                                    
        return mask
    
    def prettyprint(self):
        
        printing_job = "" #lawl
        for i in range(self.map.shape[0]):
            for j in range(self.map.shape[1]):
                y = self.state[i][j]
                if y in ('|','m','?',','):
                    printing_job += y
                elif y == '':
                    printing_job += '.'
                elif '/' in y:
                    printing_job += str(self._find_item_at_position(self.players,(i,j)))   
                elif '*' in y:
                    printing_job += '*'
                elif 'mm' in y:
                    printing_job += 'M'
            printing_job += '\n'

        print(printing_job)
       
       
    def start(self, limited_view=True):
        """start and play a game"""
        self.reset()        

        previous_view = [None for i in range(self.ginfo.nb_players)]
        
        if limited_view:
            persistent_filters = [self.map.getmapshapedarray(False) for i in range(self.ginfo.nb_players)]
                
        while True :
            battlefield = self.create_map_view(False,False)
            #Affichage
            if self.display :
                print("\nTurn %i" % self.ginfo.counter)
                self.prettyprint()
            
            #Retrieve an action from each player
            commands = []
            for pid in self.players_alive : 
            
                p0,p1 = self.players[pid].pos
                a = deepcopy(battlefield)
                a[p0][p1] ='o'
                if limited_view :
                    x = self.limited_view_mask((p0,p1))
                    a = self.apply_filter(a,x,persistent_filters[pid])
                    
                commands.append((pid,self.decision_functions[pid](self.ginfo, self.players[pid], a, previous_view[pid])))
                previous_view[pid] = a
                                 
            #Applying actions                
            self.apply_actions(commands)
            
            #See if terminal state
            if len(self.players_alive) <= 1 or self.ginfo.counter >= self.ginfo.iteration_limit :
                break
            
            self.ginfo.counter += 1    

        if self.ginfo.counter >= self.ginfo.iteration_limit:
            print("Iteration limit reached!")
        else :       
            print("And the winner is "+str(self.players_alive))
        
        return self.players_alive

        
    def _parse_direction(self,string):
        """ cast 'UP' to 0,1 'DOWN' to 0,-1 'LEFT' to -1,0 and 'RIGHT' to 1,0 """
        if string == "UP" :
             return -1,0
        elif string == "DOWN" :
            return 1,0
        elif string == "LEFT" :
            return 0,-1
        elif string == "RIGHT" :
            return 0,1

    def position_on_board(self,x1,x2):
        """certified that a orthogonal position is on the board """ 
        return min(x1,x2,self.map.shape[0]-(x1+1),self.map.shape[1]-(x2+1)) >=0 
                 
    def apply_actions(self,actions):
        """
        L'ordre d'application des ordres des tanks est aléatoire. À chaque tour, les paires player_id - action sont mélangées et puis sont exécutées séquentiellement.  
        """
        random.shuffle(actions)
        while(len(actions) > 0):

            player_id, act = actions.pop()
            if self.display :
                print("Player %i" % player_id + " : "+ act)       
   
            if reg_valid.match(act) is None:
                continue
            
            x1,x2 = self.players[player_id].pos
            
            
            if act[:4] == "NOPE":
                pass
            #Applying drop mine
            elif act[:4] == "MINE":
                p = self.players[player_id]
                if  p.mines_left > 0:    
                    m = Item('m',(x1,x2))
                    m.player = player_id
                    self.mines.append(m)
                    self.state[x1][x2] +='m'
                    p.mines.append((x1,x2))
                    p.mines_left -= 1        
            #Applying shoot
            elif act[:5] == "SHOOT":

                d1,d2 = self._parse_direction(act[6:])
                y1, y2 = x1+d1,x2+d2
                
                if self.position_on_board(y1,y2) and not self.map.walls[y1][y2]:
                    
                    if '/' in self.state[y1][y2]:
                        target_id = self._find_item_at_position(self.players,(y1,y2))
                        self.apply_damage(target_id,20)
                    elif 'm' in self.state[y1][y2] :
                        if 'm' in self.state[y1][y2]:
                            
                            for i in range(self.state[y1][y2].count('m')): 
                                m = self.mines.pop(self._find_item_at_position(self.mines, (y1,y2)))
                                self.players[m.player].mines.remove(m.pos)                     
                            self.state[y1][y2] = str.replace(self.state[y1][y2],'m','')         
                    else :
                        x = Item('*', (y1,y2))
                        x.direction = (d1,d2)
                        self.bullets.append(x)
                    
            #Applying move
            elif act[:4] == "MOVE":
                d1,d2 = self._parse_direction(act[5:])
                y1,y2 = x1+d1,x2+d2
                if self.position_on_board(y1,y2) and not self.map.walls[y1][y2]: 
                    if '/' in self.state[y1][y2]: #A player is already on that tile
                        continue
                    if '*' in self.state[y1][y2]: #A bullet is on that tile
                        for x in range(self.state[y1][y2].count('*')):
                            self.apply_damage(player_id,20)
                            self._remove_item_at_position(self.bullets, (y1,y2))
                        self.state[y1][y2] = str.replace(self.state[y1][y2],'*','')
                                            
                    if 'm' in self.state[y1][y2]: # A mine is on that tile
                        
                        for x in range(self.state[y1][y2].count('m')):
                            m = self._find_item_at_position(self.mines, (y1,y2))
                            
                            if self.mines[m].player == player_id:
                               break
                            else :
                                m = self.mines.pop(m)
                                self.players[m.player].mines.remove(m.pos)
                                self.state[y1][y2] = str.replace(self.state[y1][y2],'m','')    
                                self.apply_damage(player_id,30)

                    
                    if self.players[player_id].life_left > 0:                
                        self.move_object(self.players[player_id],d1,d2)
                    
                    
        #making those bullets move
        self.iterate_bullets()            

    def apply_damage(self,player_id,dmg):
        """apply damage to a player if he's not already dead. If player's life is <= 0 after damage is applied then it is remove from the board and the self.players _alive set"""
        p = self.players[player_id]
        if p.life_left<=0:
            return
                    
        p.life_left -= dmg
        if self.display:
            print("Player"+str(player_id)+" took "+str(dmg)+" damages and now has "+str(p.life_left)+" life left.")
        
        if p.life_left <= 0 :
            self.remove_object(self.players[player_id])
            self.players_alive.remove(player_id)
            
    def _remove_item_at_position(self, l, pos):
        """ l is a list of Item objects
            pos is a size 2 tuple that represent a position
            
            This fonction removes the first object of l that has the same position value as variable pos
                """
        return l.pop(self._find_item_at_position(l,pos))

    def _find_item_at_position(self, l, pos):
        """ l is a list of Item objects
            pos is a size 2 tuple that represent a position
            
            This fonction returns the first object of l that has the same position value as variable pos
                """
        i=0
        for x in l:
            if x.pos[0] == pos[0] and x.pos[1] == pos[1]:
                return i
            else :
                i += 1
        return i    
    
            
    def iterate_bullets(self):
        """make all the bullets move 2 tiles in their given direction. Resolve colision with wall, tanks and mines. Collision with other bullets are ignored."""
        i=0
        n = []
        while len(self.bullets) != 0:
            
            b = self.bullets.pop()
            keep_bullet = True
            for z in range(2): #Because bullets move 2 tiles by turn
                y1,y2 = b.direction[0]+b.pos[0], b.direction[1]+b.pos[1]
                
                if self.position_on_board(y1,y2) and not self.state[y1][y2] == '|':
                    
                    if '/' in self.state[y1][y2]: #Collision with a player
                        target_id = self._find_item_at_position(self.players,(y1,y2))
                        self.apply_damage(target_id,20)
                        keep_bullet=False
                        break
                    elif 'm' in self.state[y1][y2] : #Collision with at least a mine. Removes all mine on tile.         
                        for x in range(self.state[y1][y2].count('m')):
                            m = self._remove_item_at_position(self.mines, (y1,y2))
                            self.players[m.player].mines.remove(m.pos)
                        self.state[y1][y2] = str.replace(self.state[y1][y2],'m','')
                        
                        keep_bullet = False
                        break      
                    else:                                 
                        self.move_object(b,b.direction[0], b.direction[1])
                        #b.pos = b.pos[0] + b.direction[0], b.pos[1] + b.direction[1] 
                else:
                    keep_bullet = False
            if keep_bullet:
                n.append(b) 
            else :
                self.state[b.pos[0]][b.pos[1]] = str.replace(self.state[b.pos[0]][b.pos[1]],'*','')
                
        
        self.bullets = n
    
    
    def move_object(self, obj, d0, d1):
        """ assumes the move is legal. actualize state. """
        self.state[obj.pos[0]][obj.pos[1]] = str.replace(self.state[obj.pos[0]][obj.pos[1]],obj.label,'')        
        obj.pos = obj.pos[0]+d0,obj.pos[1]+d1
        self.state[obj.pos[0]][obj.pos[1]] += obj.label
        
    def remove_object(self, obj):
        """  """
        y1,y2 = obj.pos[0], obj.pos[1]
        self.state[y1][y2] = str.replace(self.state[y1][y2],obj.label,'')        
        
class Item:
#      A general item template for bullet and mines. Bullets instances will have an attribute direction and mines will have an attribute player.
    def __init__(self,label, position): 
        self.label=label
        self.pos=position
    
class Player(Item):
    def __init__(self,player_id, position, initial_life,initial_mines):
        Item.__init__(self,"/"+str(player_id),position)
        self.id = player_id
        self.life_left = initial_life
        self.mines_left = initial_mines
        self.mines = []
        
class Map :
    def __init__(self, walls, initial_pos):
        """ 
        walls is a 2D boolean array where each   
        initial_pos : initial player positions
        
        """
        self.walls = walls
        self.initial_pos = initial_pos
        self.shape = len(self.walls), len(self.walls[0])

    def getmapshapedarray(self,fill):
        return [[fill for i in range(self.shape[1])] for i in range(self.shape[0])]
###  
## MAPS 
###
# Les différentes cartes possibles, vous pouvez générer vos propres maps. Les maps ici présentés ne seront pas nécessairement celles sur lesquelles sera testés vos ias.
def handmaded1():
    """between 2 and 4 players """
    walls = [[0,0,0,0,0,0,0,0,0],
             [0,1,1,1,0,1,0,1,0],
             [0,0,0,0,0,1,0,1,0],
             [0,1,1,1,0,1,0,1,0],
             [0,0,0,0,0,0,0,0,0]]
    initial_pos = [(0,0),(4,8),(0,8),(4,0)]
    
    return Map(walls, initial_pos)        

def empty_map(shape):
    """ shape must be a 2-tuple, max 4 player"""
    walls = [[0 for i in range(shape[0])] for j in range(shape[1])]
    initial_pos = [(0,0),(shape[0]-1,shape[1]-1), (shape[0]-1,0), (0,shape[1]-1)]
    return Map(walls, initial_pos)
        
def default_map(size=20,nb_players=4):
    """nb_player doesnt do anything for now. 4 player max """
    assert size > 2
    a = [[0 for i in range(size)]for j in range(size)]
    
    for i,j in product(range(2, size-2, 2),range(2, size-2, 2)):
            a[i][j] = 1

    initial_pos = [(0,0),(size-1,size-1), (size-1,0), (0,size-1)]            
            
    return Map(a,initial_pos)

##
# LA PARTIE QUI VOUS INTÉRESSE
##
# Voici un example de démarrage de partie en python   
        
def Random(game_info, player_state, battlefield, last_turn):
    # Actions possibles : ["MOVE X", "SHOOT X", "MINE","NOPE"]
    # où X dans l'action MOVE et SHOOT représente une direction. 
    # Directions possibles : ["UP","DOWN","LEFT", "RIGHT"]
    a = random.choice(["MOVE", "SHOOT", "MINE", "NOPE"])
    
    if a == "MOVE" or a == "SHOOT":
        a += " " +random.choice(["UP","DOWN","LEFT", "RIGHT"])
    return a    
        
if __name__ == '__main__':

    #handmaded1(), default_map(25)
    gm = GameManager([Random]*4,empty_map((5,5)),initial_life=50, max_mine=5, iteration_limit=300,display=True)
    gm.start(limited_view=False)    
    
    
    
