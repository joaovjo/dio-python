# pokeapi/controllers/pokemon_controller.py
from services.api import pokemon
from urllib.parse import parse_qs

# pokeapi/controllers/pokemon_controller.py
def handle_pokemon_request(query_string):
    try:
        # Aqui o código busca o ID e a chave (como feito antes)
        id, key = parse_query_string(query_string)  # Exemplo de função para pegar o ID e a chave
        pokemon = pokemon(id)  # Função que faz a requisição da API e retorna os dados
        
        if key in pokemon['pokemons']:
            return pokemon['pokemons'][key], 200  # Retornando os dados com sucesso (status 200)
        else:
            return {"error": "Chave não encontrada"}, 404  # Erro caso a chave não exista
    
    except Exception as e:
        return {"error": str(e)}, 400  # Erro genérico, caso algum problema ocorra
