#Compétition d'AI en Python

Pour cette épreuve d'intelligence artificielle, le participant doit écrire un programme en python qui joue à une version discrète du jeu de tank. Son programme affrontera celui des autres participants et des points seront accordés aux participants en fonction du nombre de victoires de leur programme.


###Description du jeu

- À chaque étape, le tank peut faire une des actions suivante : se déplacer ("MOVE x"),  tirer ("SHOOT x"), déposer une mine ("MINE") ou ne rien faire ("NOPE"). Les actions de déplacement et de tir doivent être accompagné d'une direction $ x \in \{\text{UP, DOWN, LEFT, RIGHT}\}$. 
- Lorsque tirés, les balles apparaissent sur la case adjacente au joueur dans la direction spécifiée. Elles se déplacent de 2 cases par tour dans la direction donnée jusqu'à ce qu'un mur, un ennemi ou une mine soit percuté. 
- Les murs sont indestructibles et infranchissables.
- Les tanks possèdent 50 points de vies en début de partie, les tirs font 20 dégâts et les mines en font 30. Les balles et les mines disparaissent 
- Les mines sont invisibles aux yeux des ennemis.
- Tous les joueurs possèdent le même nombre fini de mine en début de partie. Il n'est pas possible de récupérer une mine déjà placée ni d'obtenir des mines supplémentaires.
- Les balles précédemments tirées ne disparaissent pas lorsqu'un tank est détruit. 
- Les mines précédemments déposées disparaissent lorsqu'un tank est détruit.
- Un tank ne déclenche pas une mine qu'il a lui-même posé en roulant dessus. Par contre, il peut faire exploser sa propre mine en tirant dans sa direction.


###Déroulement des tours
Tous les tanks reçoivent l'état de la partie et puis choisissent une action à poser. L'ordre d'exécution des actions est aléatoire (ce qui fait de ce jeu de tank un jeu stochastique). Une fois toutes les actions appliquées, les balles se déplacent de 2 cases. Le jeux termine si il reste un joueur ou moins, sinon, on passe au prochain tour. 

###Configuration de la partie
Le jeu possède certains paramètres auquel votre AI doit s'adapter. Le nombre maximum de mine que peut poser votre tank en est un. Le nombre maximum de tour que peut durer une partie en est un aussi. Bien qu'un paramètre de la partie, le nombre de vies initial sera toujours 50 lorsque vos ias seront évaluées. 

###Signature de la fonction de décision

La fonction qui prend une décision possède la signature suivante :

    def play(game_info, player_state, battlefield, last_turn)
        pass

        
Le nom de votre fonction n'importe pas. Voici les détails sur les variables en entrées. 'game_info' et 'player_state' sont des objets avec les attributs suivants:

- game_info.iteration_limit : Nombre de tour maximal dans la partie
- game_info.max_mine : Un entier représentant le nombre maximal de mine autorisée par joueur
- game_info.initial_positions : Une liste de paire d'entier contenant les emplacements de départ possibles (peut être plus grande que le nombre de joueur).
- game_info.turn : le compteur de tours
- game_info.nb_players : le nombre de joueurs.
- player_state.position : un tuple contenant 2 entiers indiquant la  position du tank du joueur
- player_state.life_left : le nombre de points de vies restants au tank.
- player_state.mine_left : le nombre de mines restantes au tank.
- player_state.mines : une liste contenant des paires de 2 entiers indiquants les positions des mines précédemment placé par le tank et qui n'ont pas encore explosées.

La variable battlefield est une matrice 2d (une liste de liste) de string. 

Voici les caractères que vous pouvez voir dans cette carte :

- '|' : indique un mur.
- '*' : représente une balle. Il peut y avoir plus d'une balle sur un territoire
- 'o' : représente le joueur.
- 'x' : représente un ennemi.
- '' : représente une case vide.

La variable last_turn est correspond à la variable battlefield du tour précédent.

###Champs de bataille
Plusieurs champs de bataille très simple vous sont fournis. Il vous est possible de faire vos propres cartes pour tester votre ia.

###Variante

Une variante avec information partielle sur l'état est disponible. Dans cette version, la signature de la fonction de décision est la même. Toutefois, chaque tank possède un champs de vision de 360 degrés mais qui peut être bloqué par un mur. Les cases dont l'état est inconnu sont marqués par le caractère '?'. Un mur précédemment vu est retenu pour toute la durée de la partie. Un chemin précédemment vu mais qui n'est pas présentemment dans le champ de vision du tank est marquée par ','.

Vous pouvez implémenter un AI pour cette variante pour des points bonis.

#Affichage
Il est possible d'avoir une vue de la partie en cours en passant le paramètre display=True lors de l'instanciation du GameManager. Soyez conscient que la représentation imprimée ne correspond pas à ce que votre function reçoit en entrée. L'affichage contient notamment les mines ('m' pour une mine, 'M' pour plusieurs mines) ainsi que les identifiants des joueurs.

###Avertissements et conseil

- Il est interdit d'utiliser une mémoire persistante. Vous devez programmer une fonction de décision, pas un programme avec un état interne.
- Il est interdit de modifier les objects en entrée de votre fonction. Utilisez la fonction *deepcopy()* au besoin.
- Le temps de calcul n'est pas explicitement contraint. Toutefois, un temps de calcul déraisonnable entraine une disqualification.

##Programme

Le programme est un méchant paquet de code. Je l'ai terminé un peu à la va-vite. Veuillez me signaler tout bug rencontré.

###Instanciation et démarrage de partie.
Vous pouvez coder votre fonction directement dans le fichier *tank.py* et puis appeler le fichier avec la commande 'python tank.py'. Un exemple d'initialisation de partie se retrouve à la fin du fichier. 

###Modification du programme
Vous pouvez modifier ce programme à votre guise tant que ça ne change pas le déroulement du jeu. Comme mentionné précédemment, vous pouvez aussi coder vos propres cartes. Vous pouvez me transmettre vos modifications et cartes si vous voulez que je les rajoute sur le dépôt. Partager ses cartes témoigne d'un bon esprit sportif. C'est clair que je prends ça en compte lors de l'évaluation.


