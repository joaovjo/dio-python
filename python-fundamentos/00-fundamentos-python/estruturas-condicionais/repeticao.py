# texto = input('Digite um texto: ')
# VOGAIS = 'AEIOU'

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end=' ')

# else:
#     print()
#    print('Fim do programa')

# for numero in range(0, 30, 2): # range(inicio, fim, passo) - inicio e passo são opcionais, fim é obrigatório - range retorna uma sequência de números
#     print(numero, end=' ')
    
while True:
    texto = input('Digite um texto: ')
    if texto == 'sair':
        break
    print(texto)