# No fatiamento de strings é necessário especificar o start, stop e step.
# O start é o índice onde a fatia começa, o stop é o índice onde a fatia termina e o step é o intervalo entre os índices.

nome = "João Vitor de Jesus Oliveira"

# Fatiamento de strings
# string[start:stop:step]
print(nome[0] + "\n") # J (primeiro caractere da string)
print(nome[-1] + "\n") # a (último caractere da string)
print(nome[0:4] + "\n") # João
print(nome[5:10] + "\n") # Vitor
print(nome[11:13] + "\n") # de
print(nome[14:19] + "\n") # Jesus
print(nome[20:28] + "\n") # Oliveira

print(nome[:] + "\n") # João Vitor de Jesus Oliveira (copia a string inteira)

# Fatiamento de strings com step
# string[start:stop:step]
print(nome[::-1] + "\n") # arievilO suseJ ed rotiV oãoJ (inverte a string)