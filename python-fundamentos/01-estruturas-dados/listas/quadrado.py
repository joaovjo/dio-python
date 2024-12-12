numeros = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]

quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)
    
print(quadrados)

numeros = [74, 55, 64, 45, 12, 93, 42, 87, 20, 61, 72, 3, 12, 45, 28, 1, 64, 73, 74, 21] 

quadrados = []

quadrados = [numero ** 2 for numero in numeros]

print(quadrados)