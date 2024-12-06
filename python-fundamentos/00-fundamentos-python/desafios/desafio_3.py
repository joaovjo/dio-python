def conta_vogais(texto):
    vogais = "aeiouAEIOU" # Definimos uma string com todas as vogais
    
    contador = 0 # Inicializamos um contador com o valor 0
    
    # Iteramos sobre cada caractere da string texto
    for char in texto: # Para cada caractere char na string texto
        if char in vogais: # Se o caractere char estiver na string vogais
            contador += 1 # Incrementamos o contador em 1
    return contador # Retornamos o valor do contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")