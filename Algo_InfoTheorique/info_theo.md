
###Algorithmie

1. Une machine doit redonner $x < 100$ sous à un client. Elle possède une quantité illimitée de pièce de 5, 10, 25. Écrivez une fonction qui calcul le change à redonner.

2. Cette même machine possède désormais une quantité limitée de pièce de 5, 10 et 25 sous. Écrivez un algorithme qui prends en compte cette contrainte.


######La machine
Considérez 1 ligne d'assemblage multi-fonctionnelle et une liste de tâches à accomplir, ainsi que leur dépendances.

Par exemple, A, B, C, D sont des tâches. Ces tâches ont les dépendances suivantes :
- A doit être faite avant B et C
- B doit être faite avant D
- C doit être faite avant D

1. Donnez un algorithme qui planifie l'ordre d'exécution en respectant les priorités.

2. On suppose maintenant $M$ lignes d'assemblages qui travaillent en simultané. Décrivez un algorithme qui permet de planifier de façon optimale la distribution des tâches entre chaque ligne d'assemblage. Considérez que toutes les tâches ont la même durée.

3. Considérez maintenant que les tâches ne durent pas le même nombre de temps. Est-il possible d'élaborer un algorithme qui résoud ce problème en temps polynomial? Si oui, décrivez-le. Sinon, donnez en un qui n'est pas polynomial.


### Complexité du calcul

1. Quel support de mémoire utilise une machine de Turing?

2. Vous devez trier un tableau qui contient des millions d'âges de personnes. Il est bien sûr possible de réussir ceci en utilisant un simple quick sort, mais est-il possible de réaliser un tri en O(n)? Si oui, lequel? Sinon, pourquoi?

3. Sous la prémisse que nous possédons un éditeur de niveau de mario bros et que nous pouvons contruire dynamiquement des niveaux avec les objets (murs, koopa), il est possible de prouver que Mario Bros est NP-Complet. Discuter de cette affirmation. 

4. Définissez la classe NL. Donnez un exemple de langage NL-Complet. (points boni si il y a une preuve de NL-complétude)


### Circuits booléens

Vous recevez en entrée un circuit booléen C de n entrées et possède un seul bit de sortie. Vous savez que ce circuit est borné par une profondeur de q(n). Donner une façon d'évaluer ce circuit qui utilise un espace dans O(q(n))


### Combinatoire :

Dans un graphe, un chemin élémentaire entre un sommet A et un sommet B est défini comme une séquence d'arcs uniques qui possèdent comme sommet d'origine le sommet d'arrivée du précédent. Le premier arc débute au sommet A et le dernier arc termine à B.

Soit la classe de graphe non-directionné $Q$, où $Q_n$ est un graphe de la même forme qu'un cube en $n$ dimensions. $Q_3$ est un cube en 3 dimension, $Q_2$ est un carré, $Q_1$ est une ligne et $Q_0$ est un point.  Voir le fichier cubes.png pour un support visuel


Soit le graphe $Q_3$ de forme cubique et les sommets A et B qui situés en diagonale l'un de l'autre. Combien y a-t-il de chemins élémentaires distincts entre le sommet A et B?


Soit $Q_4$, un hyper-cube en 4 dimensions, et les sommets indiqués dans le fichier cubes.png. Combien y a-t-il de chemin élémentaires distincts du sommet A au sommet B? de A à C? de A à B en passant par C?

###Crypto

Alice veut parler à Bob. Ils ont une ligne de communication non-fiable. Il existe une probabilité de 0.25 que le bit qu'Alice envoi soit inversé. En utilisant la meilleure stratégie possible, quel est le nombre moyen de bits qu'Alice doit envoyer si elle veut communiquer $n$ bits choisis aléatoirement?


