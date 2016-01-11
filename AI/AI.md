#Compétition d'AI en Python

Pour cette épreuve d'intelligence artificielle, le participant doit écrire un programme en python qui joue à une version discrète du jeu de tank. Son programme affrontera celui des autres participants et des points seront accordés aux participants en fonction du nombre de victoires de leur programme.


###Description du jeu

- À chaque étape, le tank peut faire une des actions suivante : se déplacer ("MOVE x"),  tirer ("SHOOT x"), déposer une mine ("MINE") ou ne rien faire ("NOPE"). Les actions de déplacement et de tir doivent être accompagné d'une direction $ x \in \{\text{UP, DOWN, LEFT, RIGHT}\}$. 
- Lorsque tirés, les obus apparaissent sur la case adjacente au joueur dans la direction spécifiée. Elle se déplacent de 2 cases par tour dans la direction donnée jusqu'à ce qu'un mur, un ennemi ou une mine soit percuté. 
- Les murs sont indestructibles et infranchissables
- Les tanks possèdent 50 points de vies en début de partie, les tirs font 20 dégâts et les mines en font 30. Les balles et les mines disparaissent 
- Les mines sont invisibles aux yeux des ennemis.
- Tous les joueurs possèdent le même nombre fini de mine en début de partie. Il n'est pas possible de récupérer une mine déjà placer ni d'obtenir des mines supplémentaires.
- Les balles précédemments tirés ne disparaissent pas lorsqu'un tank est détruit. 
- Les mines précédemments déposées disparaissent lorsqu'un tank meurt.
- Un tank ne déclenche pas une mine qu'il a lui-même posé en roulant dessus. Par contre, il peut faire exploser sa propre mine en tirant dans la direction.


###Déroulement des tours
Tous les tanks reçoivent l'état de la partie et puis choisissent une action à poser. L'ordre d'exécution des actions est aléatoire (ce qui fait de ce jeu de tank un jeu stochastique). Une fois toutes les actions appliquées, les balles se déplacent de 2 cases. Le jeux termine si il reste un joueur ou moins, sinon, on passe au prochain tour. 

###Configuration de la partie
Le jeux possède certains hyper-paramètres auquel votre AI doit s'adapter. Le nombre maximum de mine que peut poser votre tank en est un. Le nombre maximum de tour que peut durer une partie en est un aussi.

###Champs de bataille.
Plusieurs champs de bataille très simple vous sont fournis. Il vous est possible de faire vos propres cartes pour vos entrainer.

###Signature de la fonction qui joue.

La fonction qui prend une décision possède la signature suivante :

    def play(game_info, player_state, battlefield, last_turn)
        pass

        
Voici les détails sur les variables en entrées. 'game_info' et 'player_state' sont des objets avec les attributs suivants:

game_info.iteration_limit : Nombre de tour maximal dans la partie
game_info.max_mine : Un entier représentant le nombre maximal de mine autorisée par joueur
game_info.initial_positions : Une liste de paire d'entier contenant les emplacements de départ possibles (peut être plus grande que le nombre de joueur).
game_info.turn : le compteur de tour
player_state.position : un tuple contenant 2 entier indiquant la position du tank du joueur
player_state.life_left : le nombre de vie restante au tank du joueur
player_state.mine_left : le nombre de mine restante au joueur
player_state.mines : une liste contenant des paires de 2 entier indiquant les positions des mines qu'il a placé sur la carte et qui n'ont pas encore explosées.

La variable battlefield est une matrice 2d (une liste de liste) de string. 

Voici les caractères que vous pouvez voir dans cette carte :
'|' : indique un mur.
'*' : représente une balle. Il peut y avoir plus d'une balle sur un territoire
'o' : représente le joueur
'x' : représente un ennemi.
'.' : représente une case vide

La variable last_turn est correspond à la variable battlefield du turn précédent.

###Variante

Une variante avec information partielle sur l'état est disponible. Dans cette version, la signature de la fonction de décision est la même. Toutefois, chaque tank possède un champs de vision de 360 degrés mais qui peut être bloqué par un mur. Les cases dont l'état est inconnu sont marqués par le caractère '?'.

Vous pouvez implémenter un AI pour cette variante pour des points bonis.

###Avertissement et conseil

- Il est interdit d'utiliser une mémoire persistante. Vous devez programmer une fonction de décision, pas un AI avec un état interne.
- Le temps de calcul n'est pas explicitement contraint. Toutefois, un temps de calcul déraisonnable entraine une disqualification. Il n'est pas recommandé d'utiliser des techniques de type "brute-force".

##Programme

*Programme pas encore terminé, il sera mis sur github et vous serez contacté quand il sera fini*

###Appel du programme


