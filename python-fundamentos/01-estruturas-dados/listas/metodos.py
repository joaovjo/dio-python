# [].append - adiciona um item ao final da lista

lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

# .copy() - copia uma lista para outra

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

# [].count - conta quantas vezes um elemento aparece na lista

cores = ["azul", "verde", "amarelo", "vermelho", "azul", "verde", "azul"]

print(cores.count("azul"))
print(cores.count("verde"))
print(cores.count("amarelo"))

# [].extend - adiciona elementos de uma lista a outra

linguagens = ["Python", "Java", "C++"]

print(linguagens)

linguagens.extend(["Ruby", "JavaScript", "PHP"])

print(linguagens)