# pokeapi/utils/http_utils.py
import json

def send_json_response(request_handler, data, status_code=200):
    # Definindo a resposta JSON
    response = json.dumps(data).encode('utf-8')

    # Enviando a resposta
    request_handler.send_response(status_code)
    request_handler.send_header("Content-Type", "application/json")
    request_handler.send_header("Content-Length", str(len(response)))
    request_handler.end_headers()
    request_handler.wfile.write(response)
