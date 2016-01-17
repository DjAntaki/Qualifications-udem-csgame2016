
Algorithmie
===========
1.a Une machine doit redonner $x <= 100$ sous à un client. Elle possède une quantité illimitée de pièce de 5, 10, 25. Écrivez une fonction qui calcul le change à redonner.

1.b Cette même machine possède désormais une quantité limitée de pièce de 5, 10 et 25 sous. Écrivez un algorithme qui prends en compte cette contrainte.


2.La machine
Considérez 1 ligne d'assemblage multi-fonctionnelle et une liste de tâches à accomplir, ainsi que leur dépendances.

Par exemple, A, B, C, D sont des tâches. Ces tâches ont les dépendances suivantes :
- A doit être faite avant B et C
- B doit être faite avant D
- C doit être faite avant D

2.a Donnez un algorithme qui planifie l'ordre d'exécution en respectant les priorités.

2.b On suppose maintenant $M$ lignes d'assemblages qui travaillent en simultané. Décrivez un algorithme qui permet de planifier de façon optimale la distribution des tâches entre chaque ligne d'assemblage. Considérez que toutes les tâches ont la même durée.

2.c Considérez maintenant que les tâches ne durent pas le même nombre de temps. Est-il possible d'élaborer un algorithme qui résoud ce problème en temps polynomial? Si oui, décrivez-le. Sinon, donnez en un qui n'est pas polynomial.

Combinatoire 
============

Dans un graphe, un chemin élémentaire entre un sommet A et un sommet B est défini comme une séquence d'arcs uniques qui possèdent comme sommet d'origine le sommet d'arrivée du précédent. Le premier arc débute au sommet A et le dernier arc termine à B.

Soit la classe de graphe non-directionné $Q$, où $Q_n$ est un graphe de la même forme qu'un cube en $n$ dimensions. $Q_3$ est un cube en 3 dimension, $Q_2$ est un carré, $Q_1$ est une ligne et $Q_0$ est un point.  Voir le fichier cubes.png pour un support visuel


Soit le graphe $Q_3$ de forme cubique et les sommets A et B qui situés en diagonale l'un de l'autre. Combien y a-t-il de chemins élémentaires distincts entre le sommet A et B?


Soit $Q_4$, un hyper-cube en 4 dimensions, et les sommets indiqués dans le fichier cubes.png. Combien y a-t-il de chemin élémentaires distincts du sommet A au sommet B? de A à C? de A à B en passant par C?

Crypto
======

Alice veut parler à Bob. Ils ont une ligne de communication non-fiable. Il existe une probabilité de 0.25 que le bit qu'Alice envoi soit inversé. En utilisant la meilleure stratégie possible, quel est le nombre moyen de bits qu'Alice doit envoyer si elle veut communiquer $n$ bits choisis aléatoirement?



Complexité du calcul
====================

1. Quel support de mémoire utilise une machine de Turing?

2. Vous devez trier un tableau qui contient des millions d'âges de personnes. Il est bien sûr possible de réussir ceci en utilisant un simple quick sort, mais est-il possible de réaliser un tri en O(n)? Si oui, lequel? Sinon, pourquoi?

3. Sous la prémisse que nous possédons un éditeur de niveau de mario bros et que nous pouvons contruire dynamiquement des niveaux avec les objets (murs, koopa), il est possible de prouver que Mario Bros est NP-Complet. Discuter de cette affirmation. 

4. Définissez la classe NL. Donnez un exemple de langage NL-Complet. (points boni si il y a une preuve de NL-complétude)

5. Pour ce problème, nous allons vous présenter le tri bitonique fusion. C'est un 
algorithme de tri intéressant parce qu'il se parallélise bien, ce qui lui permet
d'obtenir une complexité parallèle d'ordre inférieure à O(n log(n)). 

La particularité de cet algorithme est de d'abord former une suite bitonnique
pour ensuite trier efficacement la suite. Une suite bitonique est une suite telle
que x_0 <= ... <= x_k >= ... >= x_{n-1} pour un k tel que 0 <= k < n.

Pour ce problème, nous vous demandons d'analyser la complexité par rapport au 
nombre de comparaison de la version séquentielle de cet algorithme qui se
trouve dans le fichier bitonic_sort.c.

(bonus) Parallélisez l'algorithme et montrez sa complexité. Indice, il faut
regarder comment s'effectuent les “swap”.

6. Vous recevez en entrée un circuit booléen C de n entrées et possède un seul bit de sortie. Vous savez que ce circuit est borné par une profondeur de q(n). Donner une façon d'évaluer ce circuit qui utilise un espace dans O(q(n))

Classification de problèmes
===========================

Pour chacun des problèmes suivants, indiquer sa classe de complexité (la plus proche), 
ainsi que s'il est complet ou hard pour cette classe. Indiquez le théorème ou la réduction 
(logarithmique, polynomiale, multivoque ou de Turing) qui vous permet de facilement 
classifier chacun des problèmes.

Par exemple:
>
> Le problème 3-col est Np-Complet car il se réduit polynomialement au problème 3-Sat.
> Aussi, 3-Col se vérifie facilement en temps polynomial.
>


Les complexités sont (leurs compléments, s'ils sont définit, sont admis): 
 * Polynomiale (P), 
 * Hors-Contexte (HC), 
 * Régulier (R),
 * Hierarchie Arithmétique (HA),
 * Polynomiale Non-Déterministe (NP),
 * Logarithmique (L),
 * de Nick (NC),
 * Décidable/Récursif,
 * Reconnaissable/Récursivement énumérable,
 * Temps exponentiel et
 * Espace exponentiel.


Problèmes à classer:
 * Décider la primalité d'un nombre
 * L'ENSEMBLE des langages réguliers (pas la complexité de chacun des langages réguliers)
 * Le langage engendré par la grammaire suivante
    S ::= PS | AS | epsilon
    P ::= 1A1 | 2A2 | 3A3 | 4A4 | 5A5 | 6A6 | 7A7 | 8A8 | 9A9 | 0A0
    A ::= NNNN
    N ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
 * La recherche d'un chemin à poids minimal passant par tout les sommets dans un graphe non-dirigé
 * Le langages des expressions mathématiques simples [+, -, ×, ÷, =, ( et )] bien formées
 * Un programme qui décide si deux expressions lambda (lambda calcul) sont équivalentes
 * Les langages des dates biens formées (AAAA/MM/JJ)
 * La recherche d'un chemin de poids inférieur à D passant par chacun des sommets à l'intérieur d'un graphe non-dirigé
 * La fonction d'Ackerman
 * L'ensemble des langages finis
 * L'ensemble des machines de turing qui s'arrêtent sur chacune de leur configuration initiale possible
 * Le langage des nombres premiers inférieurs à 1000000
 * Un programme qui traduit d'un langage de programmation Turing-complet vers un autre langage Turing-complet
 * Un langage fini
 * La factorisation d'entiers

On vous demande aussi d'énoncer les relations entre les classes que vous connaissez 
i.e. 
>
> A est contenue dans B
> B est strictement contenue dans C
>

Dans l'exemple précédent, il n'est pas nécessaire de mentionner que A est strictement
contenue dans C. C'est évident par transitivité.

Fermeture
=========
Montrez qu'un langage regulier est fermé sous l'union, l'intersection, la négation,
la concaténation ainsi que la différence.
Montrez que les naturels sont fermés sous l'addition et la multiplication, mais pas
sous la soustraction et la division.


Réduction
=========

Polynomiale
-----------
Si NP correspond aux problèmes pour lesquels il existe un vérificateur en temps polynomial, 
les problèmes co-NP correspondent aux problèmes pour lesquels il est possible de vérifier
un contre exemple en temps polynomial.
Par exemple, la satisfaisabilité d'un circuit est dans NP et correspond au problème de l'existence
d'une entrée satisfaisant le circuit. Le problème équivalent dans co-NP correspond au problème
d'insatisfaisabilité, c'est-à-dire que pour tout entrée, le circuit ne peut pas être satisfait.

Montrez que le problème d'équivalence de deux circuit est dans co-NP.


Extension
=========

Vous avez la possibilité de créer d'autres problèmes en autant que vous y répondiez.
