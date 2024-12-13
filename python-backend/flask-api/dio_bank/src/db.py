import sqlite3  # Importa o módulo sqlite3 para interagir com o banco de dados SQLite
from datetime import datetime  # Importa a classe datetime para manipulação de datas e horas

import click  # Importa o módulo click para criar comandos de linha de comando
from flask import (  # Importa objetos do Flask
    current_app,  # Referência à aplicação Flask atual
    g,  # Objeto de contexto global para armazenar dados durante uma solicitação
)

"""
O objeto g é uma instância de contexto que é única para cada solicitação. 
É usado para armazenar dados que podem ser acessados por várias funções durante o ciclo de vida de uma solicitação.
"""


def get_db():  # Essa função é responsável por criar uma conexão com o banco de dados SQLite e retornar o objeto de conexão.
    if "db" not in g:  # Verifica se a conexão com o banco de dados ainda não foi criada
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )  # Cria a conexão com o banco de dados
        g.db.row_factory = sqlite3.Row  # Configura a conexão para retornar linhas como objetos Row

    return g.db  # Retorna o objeto de conexão com o banco de dados


def close_db(e=None):  # Função para fechar a conexão com o banco de dados
    db = g.pop("db", None)  # Remove a conexão com o banco de dados do objeto g

    if db is not None:  # Se a conexão existir
        db.close()  # Fecha a conexão com o banco de dados


def init_db():  # Função para inicializar o banco de dados
    db = get_db()  # Obtém a conexão com o banco de dados

    with current_app.open_resource("schema.sql") as f:  # Abre o arquivo schema.sql
        db.executescript(f.read().decode("utf8"))  # Executa o script SQL para criar as tabelas


@click.command("init-db")  # Define um comando de linha de comando chamado "init-db"
def init_db_command():  # Função que será executada quando o comando "init-db" for chamado
    """Clear the existing data and create new tables."""  # Descrição do comando
    init_db()  # Inicializa o banco de dados
    click.echo("Initialized the database.")  # Exibe uma mensagem indicando que o banco de dados foi inicializado


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)  # Registra um conversor para o tipo "timestamp" no SQLite


def init_app(app):  # Função para inicializar a aplicação Flask
    app.teardown_appcontext(
        close_db
    )  # Registra a função close_db para ser chamada quando o contexto da aplicação for encerrado
    app.cli.add_command(init_db_command)  # Adiciona o comando "init-db" à interface de linha de comando da aplicação
