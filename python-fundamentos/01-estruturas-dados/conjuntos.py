numeros = set([1,2,3,1,3,4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "uno", "palio"))
print(carros)

linguagens = {"python", "java", "python", "c", "java"}
print(linguagens)

conjunto_a = {1,2,3}
conjunto_b = {3,4,2,1}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

conjunto_a.union(conjunto_b)
conjunto_b.union(conjunto_a)

conjunto_a.intersection(conjunto_b)
conjunto_b.intersection(conjunto_a)

conjunto_a.symmetric_difference(conjunto_b)
conjunto_b.symmetric_difference(conjunto_a)

conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)

conjunto_a.issuperset(conjunto_b)
conjunto_b.issuperset(conjunto_a)

