#Comp�tition d'AI en Python

Pour cette �preuve d'intelligence artificielle, le participant doit �crire un programme en python qui joue � une version discr�te du jeu de tank. Son programme affrontera celui des autres participants et des points seront accord�s aux participants en fonction du nombre de victoires de leur programme.


###Description du jeu

- � chaque �tape, le tank peut faire une des actions suivante : se d�placer ("MOVE x"),  tirer ("SHOOT x"), d�poser une mine ("MINE") ou ne rien faire ("NOPE"). Les actions de d�placement et de tir doivent �tre accompagn� d'une direction $ x \in \{\text{UP, DOWN, LEFT, RIGHT}\}$. 
- Lorsque tir�s, les obus apparaissent sur la case adjacente au joueur dans la direction sp�cifi�e. Elle se d�placent de 2 cases par tour dans la direction donn�e jusqu'� ce qu'un mur, un ennemi ou une mine soit percut�. 
- Les murs sont indestructibles et infranchissables
- Les tanks poss�dent 50 points de vies en d�but de partie, les tirs font 20 d�g�ts et les mines en font 30. Les balles et les mines disparaissent 
- Les mines sont invisibles aux yeux des ennemis.
- Tous les joueurs poss�dent le m�me nombre fini de mine en d�but de partie. Il n'est pas possible de r�cup�rer une mine d�j� placer ni d'obtenir des mines suppl�mentaires.
- Les balles pr�c�demments tir�s ne disparaissent pas lorsqu'un tank est d�truit. 
- Les mines pr�c�demments d�pos�es disparaissent lorsqu'un tank meurt.
- Un tank ne d�clenche pas une mine qu'il a lui-m�me pos� en roulant dessus. Par contre, il peut faire exploser sa propre mine en tirant dans la direction.


###D�roulement des tours
Tous les tanks re�oivent l'�tat de la partie et puis choisissent une action � poser. L'ordre d'ex�cution des actions est al�atoire (ce qui fait de ce jeu de tank un jeu stochastique). Une fois toutes les actions appliqu�es, les balles se d�placent de 2 cases. Le jeux termine si il reste un joueur ou moins, sinon, on passe au prochain tour. 

###Configuration de la partie
Le jeux poss�de certains hyper-param�tres auquel votre AI doit s'adapter. Le nombre maximum de mine que peut poser votre tank en est un. Le nombre maximum de tour que peut durer une partie en est un aussi.

###Champs de bataille.
Plusieurs champs de bataille tr�s simple vous sont fournis. Il vous est possible de faire vos propres cartes pour vos entrainer.

###Signature de la fonction qui joue.

La fonction qui prend une d�cision poss�de la signature suivante :

    def play(game_info, player_state, battlefield, last_turn)
        pass

        
Voici les d�tails sur les variables en entr�es. 'game_info' et 'player_state' sont des objets avec les attributs suivants:

game_info.iteration_limit : Nombre de tour maximal dans la partie
game_info.max_mine : Un entier repr�sentant le nombre maximal de mine autoris�e par joueur
game_info.initial_positions : Une liste de paire d'entier contenant les emplacements de d�part possibles (peut �tre plus grande que le nombre de joueur).
game_info.turn : le compteur de tour
player_state.position : un tuple contenant 2 entier indiquant la position du tank du joueur
player_state.life_left : le nombre de vie restante au tank du joueur
player_state.mine_left : le nombre de mine restante au joueur
player_state.mines : une liste contenant des paires de 2 entier indiquant les positions des mines qu'il a plac� sur la carte et qui n'ont pas encore explos�es.

La variable battlefield est une matrice 2d (une liste de liste) de string. 

Voici les caract�res que vous pouvez voir dans cette carte :
'|' : indique un mur.
'*' : repr�sente une balle. Il peut y avoir plus d'une balle sur un territoire
'o' : repr�sente le joueur
'x' : repr�sente un ennemi.
'.' : repr�sente une case vide

La variable last_turn est correspond � la variable battlefield du turn pr�c�dent.

###Variante

Une variante avec information partielle sur l'�tat est disponible. Dans cette version, la signature de la fonction de d�cision est la m�me. Toutefois, chaque tank poss�de un champs de vision de 360 degr�s mais qui peut �tre bloqu� par un mur. Les cases dont l'�tat est inconnu sont marqu�s par le caract�re '?'.

Vous pouvez impl�menter un AI pour cette variante pour des points bonis.

###Avertissement et conseil

- Il est interdit d'utiliser une m�moire persistante. Vous devez programmer une fonction de d�cision, pas un AI avec un �tat interne.
- Le temps de calcul n'est pas explicitement contraint. Toutefois, un temps de calcul d�raisonnable entraine une disqualification. Il n'est pas recommand� d'utiliser des techniques de type "brute-force".

##Programme

*Programme pas encore termin�, il sera mis sur github et vous serez contact� quand il sera fini*

###Appel du programme


