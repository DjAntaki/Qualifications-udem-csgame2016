# -*- encoding: utf-8 -*-
"""
Faites une IA!

Vous êtes un survivant d'une apocalypse de zombies, et chaque minute compte!

Vous pouvez à chaque tour vous déplacer, ne rien faire, ou bien tirer
sur le zombie le plus proche (s'il est à moins de 8 blocs de distance).

Le but est de survivre le plus longtemps possible.

Faites attention, size (la taille du jeu) peut être bien plus grand que 15...
"""
import random
import math

playercount = 0
deaths = {}

MOVES = ["UP","DOWN","LEFT","RIGHT","SHOOT","NOP"]

def fdist(A, B):
    return math.sqrt((A[0]-B[0])*(A[0]-B[0])+(A[1]-B[1])*(A[1]-B[1]))

def dist(A, B):
    return int(fdist(A,B))

def block_norm(A):
    if abs(A[0]) > abs(A[1]):
        return [A[0]/abs(A[0]),0]
    if A[1] == 0: return [0,0]
    return [0,A[1]/abs(A[1])]

class RandomPlayer:
    def __init__(self):
        global playercount
        self.tag = chr(ord('a')+playercount)
        playercount += 1
        self.pos = [0,0]
        self.health = 50
        self.bullets = 0

    def play(self, board):
        return random.choice(MOVES)

class Board:
    def __init__(self, size=15):
        self.t = [[0 for i in range(size)] for j in range(size)]
        self.size = size
        self.zombies = []
        self.players = []

    def show(self):
        s = "|"+"-"*self.size+"|\n|"
        for i in range(self.size):
            for j in range(self.size):
                if self.t[i][j]: s += self.t[i][j]
                else: s += " "
            s += "|\n|"
        print s+"-"*self.size+"|"


    def init(self, players):
        size = self.size
        nzombies = int(size * size * 0.05)
        nbullets = int(size * size * 0.01)
        npacks   = int(size * size * 0.02)

        for i in range(nzombies):
            x,y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.t[x][y] = "Z"
            self.zombies.append([x,y])

        for i in range(nbullets):
            x,y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.t[x][y] = "B"

        for i in range(npacks):
            x,y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.t[x][y] = "H"

        for i in players:
            x,y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.t[x][y] = i.tag
            i.pos = [x,y]

        self.players = players

    def killzombiefrom(self, pos):
        closest = None
        mindist = 10000000
        for z in self.zombies:
            d = dist(pos, z)
            if d < 8 and d < mindist:
                mindist = d
                closest = z
        if closest:
            self.t[closest[0]][closest[1]] = 0
            self.zombies.pop(self.zombies.index(closest))
            print "zombie",closest,"was killed"

    def update_zombies(self):
        for z in self.zombies:
            chases = []
            for p in self.players:
                if dist(p.pos, z) < 6:
                    chases.append(block_norm([p.pos[0]-z[0],p.pos[1]-z[1]]))
            chase = random.choice(chases) if len(chases) else block_norm([random.randint(-2,2),random.randint(-2,2)])
            if 0<=z[0]+chase[0]<self.size-1 and \
                    0<=z[1]+chase[1]<self.size-1 and \
                    self.t[z[0]+chase[0]][z[1]+chase[1]] == 0:
                self.t[z[0]][z[1]] = 0
                self.t[z[0]+chase[0]][z[1]+chase[1]] = "Z"
                z[0] += chase[0]
                z[1] += chase[1]

    def update_health(self):
        for z in self.zombies:
            for p in self.players:
                if fdist(p.pos, z) < 1.42:
                    p.health -= 10
                    print p.tag,"loses 10 hp"

    def spawn(self):
        if random.random() > 0.9:
            e = random.choice(["Z","Z","Z","Z","B","H"])
            p = random.randint(0,self.size-1), random.randint(0,self.size-1)
            if self.t[p[0]][p[1]] == 0:
                self.t[p[0]][p[1]] = e
                print "Spawned",e,p

    def play(self, players):
        self.init(players)

        for turn in range(1000):
            for i in players:
                if i.health < 0:
                    print "Player",i.tag,"is dead!"
                    deaths[i.tag] = turn
                    players.pop(players.index(i))
                    continue
                move = i.play(self)
                delta = [0,0]
                if move == "UP" and i.pos[1] >= 1 and self.t[i.pos[0]][i.pos[1]-1] != "Z":
                    delta = [0,-1]
                if move == "DOWN" and i.pos[1] < self.size-1 and self.t[i.pos[0]][i.pos[1]+1] != "Z":
                    delta = [0,1]
                if move == "LEFT" and i.pos[0] >= 1 and self.t[i.pos[0]-1][i.pos[1]] != "Z":
                    delta = [-1,0]
                if move == "RIGHT" and i.pos[0] < self.size-1 and self.t[i.pos[0]+1][i.pos[1]] != "Z":
                    delta = [1,0]
                if move == "SHOOT" and i.bullets > 0:
                    self.killzombiefrom(i.pos)
                    i.bullets -= 1
                p = self.t[i.pos[0]+delta[0]][i.pos[1]+delta[1]]
                if p == "B":
                    i.bullets += 1
                    print i.tag,"gains a bullet"
                elif p == "H":
                    i.health += 10
                    print i.tag,"gains 10 hp"
                self.t[i.pos[0]][i.pos[1]] = 0
                self.t[i.pos[0]+delta[0]][i.pos[1]+delta[1]] = i.tag
                i.pos = [i.pos[0]+delta[0],i.pos[1]+delta[1]]

            if turn % 3:
                print("move")
                print(turn)
                self.update_zombies()

            self.update_health()
            self.spawn()
            self.show()
            if len(players) == 0:
                print "\nGame Over"
                print "Stopped at turn",turn
                break
        if len(players):
            print "\nGame Over"
            for i in players:
                print i.tag,"is still alive!"

b = Board()
b.play([RandomPlayer(), RandomPlayer()])

for i in deaths:
    print "Player",i,"died at turn",deaths[i]
