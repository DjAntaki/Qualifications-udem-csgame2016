#Comp�tition d'AI en Python

Pour cette �preuve d'intelligence artificielle, le participant doit �crire un programme en python qui joue � une version discr�te du jeu de tank. Son programme affrontera celui des autres participants et des points seront accord�s aux participants en fonction du nombre de victoires de leur programme.


###Description du jeu

- � chaque �tape, le tank peut faire une des actions suivante : se d�placer ("MOVE x"),  tirer ("SHOOT x"), d�poser une mine ("MINE") ou ne rien faire ("NOPE"). Les actions de d�placement et de tir doivent �tre accompagn� d'une direction $ x \in \{\text{UP, DOWN, LEFT, RIGHT}\}$. 
- Lorsque tir�s, les balles apparaissent sur la case adjacente au joueur dans la direction sp�cifi�e. Elles se d�placent de 2 cases par tour dans la direction donn�e jusqu'� ce qu'un mur, un ennemi ou une mine soit percut�. 
- Les murs sont indestructibles et infranchissables.
- Les tanks poss�dent 50 points de vies en d�but de partie, les tirs font 20 d�g�ts et les mines en font 30. Les balles et les mines disparaissent 
- Les mines sont invisibles aux yeux des ennemis.
- Tous les joueurs poss�dent le m�me nombre fini de mine en d�but de partie. Il n'est pas possible de r�cup�rer une mine d�j� plac�e ni d'obtenir des mines suppl�mentaires.
- Les balles pr�c�demments tir�es ne disparaissent pas lorsqu'un tank est d�truit. 
- Les mines pr�c�demments d�pos�es disparaissent lorsqu'un tank est d�truit.
- Un tank ne d�clenche pas une mine qu'il a lui-m�me pos� en roulant dessus. Par contre, il peut faire exploser sa propre mine en tirant dans sa direction.


###D�roulement des tours
Tous les tanks re�oivent l'�tat de la partie et puis choisissent une action � poser. L'ordre d'ex�cution des actions est al�atoire (ce qui fait de ce jeu de tank un jeu stochastique). Une fois toutes les actions appliqu�es, les balles se d�placent de 2 cases. Le jeux termine si il reste un joueur ou moins, sinon, on passe au prochain tour. 

###Configuration de la partie
Le jeu poss�de certains param�tres auquel votre AI doit s'adapter. Le nombre maximum de mine que peut poser votre tank en est un. Le nombre maximum de tour que peut durer une partie en est un aussi. Bien qu'un param�tre de la partie, le nombre de vies initial sera toujours 50 lorsque vos ias seront �valu�es. 

###Signature de la fonction de d�cision

La fonction qui prend une d�cision poss�de la signature suivante :

    def play(game_info, player_state, battlefield, last_turn)
        pass

        
Le nom de votre fonction n'importe pas. Voici les d�tails sur les variables en entr�es. 'game_info' et 'player_state' sont des objets avec les attributs suivants:

- game_info.iteration_limit : Nombre de tour maximal dans la partie
- game_info.max_mine : Un entier repr�sentant le nombre maximal de mine autoris�e par joueur
- game_info.initial_positions : Une liste de paire d'entier contenant les emplacements de d�part possibles (peut �tre plus grande que le nombre de joueur).
- game_info.turn : le compteur de tours
- game_info.nb_players : le nombre de joueurs.
- player_state.position : un tuple contenant 2 entiers indiquant la  position du tank du joueur
- player_state.life_left : le nombre de points de vies restants au tank.
- player_state.mine_left : le nombre de mines restantes au tank.
- player_state.mines : une liste contenant des paires de 2 entiers indiquants les positions des mines pr�c�demment plac� par le tank et qui n'ont pas encore explos�es.

La variable battlefield est une matrice 2d (une liste de liste) de string. 

Voici les caract�res que vous pouvez voir dans cette carte :

- '|' : indique un mur.
- '*' : repr�sente une balle. Il peut y avoir plus d'une balle sur un territoire
- 'o' : repr�sente le joueur.
- 'x' : repr�sente un ennemi.
- '' : repr�sente une case vide.

La variable last_turn est correspond � la variable battlefield du tour pr�c�dent.

###Champs de bataille
Plusieurs champs de bataille tr�s simple vous sont fournis. Il vous est possible de faire vos propres cartes pour tester votre ia.

###Variante

Une variante avec information partielle sur l'�tat est disponible. Dans cette version, la signature de la fonction de d�cision est la m�me. Toutefois, chaque tank poss�de un champs de vision de 360 degr�s mais qui peut �tre bloqu� par un mur. Les cases dont l'�tat est inconnu sont marqu�s par le caract�re '?'. Un mur pr�c�demment vu est retenu pour toute la dur�e de la partie. Un chemin pr�c�demment vu mais qui n'est pas pr�sentemment dans le champ de vision du tank est marqu�e par ','.

Vous pouvez impl�menter un AI pour cette variante pour des points bonis.

#Affichage
Il est possible d'avoir une vue de la partie en cours en passant le param�tre display=True lors de l'instanciation du GameManager. Soyez conscient que la repr�sentation imprim�e ne correspond pas � ce que votre function re�oit en entr�e. L'affichage contient notamment les mines ('m' pour une mine, 'M' pour plusieurs mines) ainsi que les identifiants des joueurs.

###Avertissements et conseil

- Il est interdit d'utiliser une m�moire persistante. Vous devez programmer une fonction de d�cision, pas un programme avec un �tat interne.
- Il est interdit de modifier les objects en entr�e de votre fonction. Utilisez la fonction *deepcopy()* au besoin.
- Le temps de calcul n'est pas explicitement contraint. Toutefois, un temps de calcul d�raisonnable entraine une disqualification.

##Programme

Le programme est un m�chant paquet de code. Je l'ai termin� un peu � la va-vite. Veuillez me signaler tout bug rencontr�.

###Instanciation et d�marrage de partie.
Vous pouvez coder votre fonction directement dans le fichier *tank.py* et puis appeler le fichier avec la commande 'python tank.py'. Un exemple d'initialisation de partie se retrouve � la fin du fichier. 

###Modification du programme
Vous pouvez modifier ce programme � votre guise tant que �a ne change pas le d�roulement du jeu. Comme mentionn� pr�c�demment, vous pouvez aussi coder vos propres cartes. Vous pouvez me transmettre vos modifications et cartes si vous voulez que je les rajoute sur le d�p�t. Partager ses cartes t�moigne d'un bon esprit sportif. C'est clair que je prends �a en compte lors de l'�valuation.


