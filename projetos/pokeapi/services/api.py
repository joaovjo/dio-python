# pokeapi/services/api.py
import requests

# Função para buscar o ID de um Pokémon a partir do nome
def get_pokemon_id(name):
    api = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}/"
    response = requests.get(api)
    try:
        res = response.json()
    except ValueError:
        return None
    return res.get('id')

# Função que busca o Pokémon e retorna a chave especificada
def pokemon(id, key=None):
    # Se o id for uma string (nome), buscar o ID numérico
    if isinstance(id, str):
        id = get_pokemon_id(id)
        if id is None:
            return None
    
    api = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(api)

    try:
        res = response.json()
    except ValueError:
        return None

    # Se uma chave for especificada, retorna o valor associado à chave
    if key:
        return res.get(key, f"A chave '{key}' não foi encontrada.")
    
    # Retorna o dicionário completo do Pokémon
    return res
