##Programmation embarquée

###Description générale:
Vous devez créer un "jeu" ou le but est de trouver le nombre aléatoire choisis en début de partie. Chaque fois que vous sélectionnez un nombre, une lumière clignotera une ou deux fois pour vous indiquer si le nombre à trouver est plus petit ou plus grand.

###Tâche 1:
Vous devez créer un afficheur binaires avec 7 led qui seront allumés ou éteintes pour représenter des 1 et des 0.

Vos leds devront être attachées aux pins de 13 à 7.

Vous devez aussi créer un sélectionneur de nombre grâce à un potentiomètre. La lecture de ce potentiomètre devra changer l'affichage des leds en temps réel.

Vous devez aussi inclure un schéma de branchement du potentiomètre.

###Tâche 2:
Quand un chiffre a été sélectionné pendant 1.6 secondes, une huitième led doit s'allummer une fois si le chiffre est plus petit que le chiffre à trouver et deux fois dans le cas contraire.

Dans le cas ou le chiffre trouvé est le bon, toutes les leds doivent s'éteindre durant 1 seconde et ensuite les leds du compteur doivent s'allumer et s'éteindre une à une en partant par celle représentant le plus petit chiffre. Chaque led doit à allumée durant 0.2 secondes et dès qu'une led s'éteint, une autre doit s'allumer.

Toutes les leds doivent ensuite clignotter 3 fois avant qu'une nouvelle partie ne commence avec un nouveau chiffre.