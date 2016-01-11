#Je voulais printer la liste des multiples de dix de 1 a 10 mais ca marche pas...
# Ce programme peut fonctionne en seulement trois lignes de code.
indexes = [range(10)]
multiples = [x * 10 for x in indexes]
print zip(indexes, multiples)
