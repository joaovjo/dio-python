# import requests # Importando a biblioteca requests
# import json # Importando a biblioteca json

# def pokemon(id): # Função que faz a requisição na API
#     api = f"https://pokeapi.co/api/v2/pokemon/{id}/" # URL da API
#     response = requests.get(api) # Fazendo a requisição na API

#     try: # Tratando a resposta da API
#         res = response.json() # Convertendo a resposta da API para JSON
#     except ValueError: # Caso a resposta não seja um JSON
#         return print("Deu ruim!") # Retorna a mensagem de erro
        
#     dict_response = {} # Dicionário que irá armazenar a resposta da API
    
#     for chave, valor in res.items(): # Loop que percorre a resposta da API
#         dict_response[chave] = valor # Adicionando a resposta da API no dicionário
    
#     pokemon = { # Dicionário que irá armazenar o nome do pokémon e a resposta da API
#         "pokemons": dict_response # Adicionando a resposta da API no dicionário
#     }
#     return pokemon # Retornando o dicionário com o nome do pokémon e a resposta da API
    
# print(f"Nome: {pokemon('1').get('name')}") # Imprimindo o nome do pokémon e a resposta da API

import requests  # Importando a biblioteca requests

def pokemon(id, key=None):  # Função que recebe id e opcionalmente a chave a ser buscada
    api = f"https://pokeapi.co/api/v2/pokemon/{id}/"  # URL da API usando o ID
    response = requests.get(api)  # Fazendo a requisição

    try:
        res = response.json()  # Convertendo a resposta da API para JSON
    except ValueError:
        return print("Deu ruim!")  # Se não for possível converter, retorna erro

    # Se a chave for fornecida, retorna o valor associado a ela
    if key:
        return res.get(key, f"A chave '{key}' não foi encontrada.")  # Retorna o valor da chave, ou mensagem de erro

    # Se a chave não for fornecida, apenas retorna o dicionário completo
    return res


# Exemplo de uso:
# Vamos buscar o Pokémon de ID 1 (Bulbasaur) e exibir a chave 'name'
print(pokemon('ditto', 'id'))  # Deve retornar 'bulbasaur'

# Podemos buscar qualquer chave do dicionário retornado pela API
#print(pokemon(1, 'height'))  # Deve retornar a altura do Bulbasaur

# Exemplo de uma chave não existente
#print(pokemon(1, 'invalid_key'))  # Deve retornar a mensagem de erro para chave não encontrada

# Se não passar nenhuma chave, retorna o dicionário completo do Pokémon
#print(pokemon(1))  # Exibe o dicionário completo do Bulbasaur
