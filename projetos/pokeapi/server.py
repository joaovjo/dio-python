# pokeapi/server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from views.pokemon_view import PokemonRequestHandler

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, PokemonRequestHandler)
    print("Servidor rodando na porta 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
