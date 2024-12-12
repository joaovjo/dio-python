# O primeiro elemento de uma lista tem índice 0, o segundo tem índice 1 e assim por diante.
# listas são mutáveis, ou seja, podemos alterar seus elementos.
# listas sempre começam com o índice 0, exceto se você especificar um índice diferente.

frutas = ['banana', 'maçã', 'uva', 'morango', 'abacaxi'] # Lista de frutas
print(frutas) # ['banana', 'maçã', 'uva', 'morango', 'abacaxi']
print(frutas[3]) # Seleção de um elemento da lista, nesse caso o índice 3 é 'morango'
print(frutas[-1]) # Seleção do elemento da lista usando número negativo, ou seja, começa do final da lista, nesse caso o índice -1 é 'abacaxi'

frutas = [] # Lista vazia
print(frutas) # []

letras = list('python') # ['p', 'y', 't', 'h', 'o', 'n']
print(letras)

numero = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numero)

carro = ['ford', 'fiat', 'chevrolet', 'volkswagen'] # Lista de carros
print(carro) # ['ford', 'fiat', 'chevrolet', 'volkswagen']