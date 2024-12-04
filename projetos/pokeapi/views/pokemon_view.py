# pokeapi/views/pokemon_view.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from utils.http_utils import send_json_response, send_text_response
from controllers.pokemon_controller import handle_pokemon_request

class PokemonRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Analisando a URL e os parâmetros
        parsed_url = urlparse(self.path)
        query_string = parsed_url.query

        # Chamando o controller para lidar com a requisição
        result, status_code = handle_pokemon_request(query_string)

        if isinstance(result, dict):  # Resposta JSON
            send_json_response(self, result, status_code)  # Passando 3 argumentos
        else:  # Resposta de erro ou texto
            send_text_response(self, result, status_code)
