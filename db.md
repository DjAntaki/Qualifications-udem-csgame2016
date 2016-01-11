## Database

### Questions théoriques

1. Nommez un avantage de la normalisation.
2. Qu'est ce qu'une clé candidate ?
3. En quoi consiste la deuxième forme normale ?

### Partie pratique.

On vous demande de concevoir une base de donnée pour classer les serres du jardin botanique de Montréal. Le jardin botanique de Montréal est divisé en serres. Une serre a un numéro, un numéro de zone de rusticité et au moins un employé qui y est rataché. Les employés ont un nom, un salaire et un id d'employé. Les serres contiennent des plantes qui ont un nom latin, un nom commun et un pays d'origine. Les plantes ont aussi une zone de rusticité et un numéro de terreau. Les terreaux ont une teneur en azote minimale, une teneur en azote courante et une date de dernier arrosage. Chaque serre est divisée en plusieurs terreaux.

Les questions sont en SQL sauf contre indication

1. Faites un diagramme ER représentant la base.
2. Codez le schéma de la base en SQL.
3. Écrivez la requête permettant de trouver toutes les plantes dans la serre no.3
4. Écrivez la requête permettant de trouver l'employé assigné uniquement à des serres paires
5. Écrivez la requête permettant de trouver tous les terreaux ayant moins d'azote que nécéssaire.
6. Écrivez la requête permettant de trouver toutes les plantes qui sont dans une serre innapropriée pour leur zone de rusticitée (+- 2)
7. Écrivez la requête précédante de en algèbre relationelle.

