numeros = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]

pares = [] # Lista vazia para armazenar os números pares
impares = [] # Lista vazia para armazenar os números ímpares

for numero in numeros: # Para cada número na lista de números
    if numero % 2 == 0: # Se o número for par
        pares.append(numero) # Função append adiciona o número à lista de pares
    else: # Se o número for ímpar
        impares.append(numero) # Função append adiciona o número à lista de ímpares

print("Números pares:", pares, "\n") # Imprime a lista de números pares
print("Números ímpares:", impares, "\n") # Imprime a lista de números ímpares

################### Versão com list comprehension ###################	

# List comprehension é uma forma mais compacta de criar listas em Python
# A lista é criada em uma única linha de código
# A sintaxe é: [expressão for item in lista if condição]
# Lê-se: Para cada item na lista, se a condição for verdadeira, adicione o item à expressão
# Nesse caso a expressão é o número, o item é o número e a condição é se o número é par ou ímpar
# A lista de números é percorrida e os números pares são adicionados à lista de pares e os ímpares à lista de ímpares
# O resultado é o mesmo, mas o código é mais enxuto

pares = [numero for numero in numeros if numero % 2 == 0] # Lista de números pares

impares = [numero for numero in numeros if numero % 2 != 0] # Lista de números ímpares

print("Números pares:", pares, "\n") # Imprime a lista de números pares
print("Números ímpares:", impares, "\n") # Imprime a lista de números ímpares