carros = ["HRV", "Golf", "Argo", "Focus"]

# Python não possui for each, mas podemos iterar sobre uma lista com o for

# Iterando a lista carros - carro é uma variável temporária que recebe cada elemento da lista até o fim do loop
# Para cada carro na lista carros, imprima o carro
for carro in carros: 
    print(carro)
print("\n")

# Podemos usar o enumerate para pegar o índice do elemento
for indice, carro in enumerate(carros): # enumerate retorna o índice e o valor
    print(f"{indice} - {carro}")