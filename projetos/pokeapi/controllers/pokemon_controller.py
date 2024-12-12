# pokeapi/controllers/pokemon_controller.py
from services.api import pokemon  # Certifique-se de importar corretamente a função de requisição da API
from urllib.parse import parse_qs


def parse_query_string(query_string):
    """Função para processar a query string e retornar os parâmetros 'id' e 'key'."""
    params = parse_qs(query_string)
    # Pega o 'id' e a 'key' a partir dos parâmetros da URL
    id_param = params.get('id', [None])[0]  # Pega o valor de 'id', se existir
    key_param = params.get('key', [None])[0]  # Pega o valor de 'key', se existir

    # Verificando se 'id' é válido
    if id_param is None:
        raise ValueError("O parâmetro 'id' é obrigatório.")
    
    return id_param, key_param


def handle_pokemon_request(query_string):
    try:
        # Aqui chamamos parse_query_string para obter 'id' e 'key'
        id, key = parse_query_string(query_string)
        
        # Usamos a função pokemon para obter os dados do Pokémon
        pokemon_data = pokemon(id)  # Certifique-se de que 'pokemon(id)' retorne um dicionário com os dados do Pokémon
        
        # Se 'key' for fornecida, tenta acessar o valor correspondente
        if key:
            if key in pokemon_data:
                return pokemon_data[key], 200  # Retorna o valor associado à chave 'key' com status 200
            else:
                return {"error": "Chave não encontrada"}, 404  # Caso a chave não exista, retorna 404
        else:
            # Se 'key' não for fornecida, retorna todo o dicionário de dados do Pokémon
            return pokemon_data, 200  # Retorna o dicionário inteiro com status 200
    
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro com status 400
        return {"error": str(e)}, 400
