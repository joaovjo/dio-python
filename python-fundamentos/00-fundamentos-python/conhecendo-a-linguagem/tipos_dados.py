string = "Hello, World!"

print(string)

# Dicionários são parecidos com JSON
# Porém JSON é um tipo de notação de dados
# Já dicionários são um tipo de DADO
# Escritas semelhantes, conceitos diferentes

# Dicionário com vários tipos de dados

thisdict = {
  "brand": "Ford", # string
  "electric": False, # booleano
  "year": 1964, # inteiro
  "colors": ["red", "white", "blue"] #array
}

# Pegue o valor do index 1 do array colors dentro do dicionário thisdict
print(thisdict.get("colors")[1])