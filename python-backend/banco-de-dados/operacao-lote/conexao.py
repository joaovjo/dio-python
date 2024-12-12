import sqlite3
from pathlib import Path

# Conexão com o banco de dados
ROOT_PATH = Path(__file__).parent

try:
    conectar = sqlite3.connect(ROOT_PATH / "database.db")  # conecta ao banco de dados
    print("Conexão realizada com sucesso!")  # mensagem de sucesso
except sqlite3.Error as erro:
    print("Erro ao conectar ao banco de dados:", erro)

try:
    cursor = conectar.cursor()  # cria um cursor para manipular o banco de dados
    print("Cursor criado com sucesso!")  # mensagem de sucesso
except sqlite3.Error as erro:
    print("Erro ao criar o cursor:", erro)


def criar_tabela(conectar, cursor, nome_tabela, campos):
    try:
        cursor.execute(  # executa um comando SQL
            f"""
                       CREATE TABLE
                        IF NOT EXISTS
                        {nome_tabela} (
                            {campos}
                        )
            """
        )
        conectar.commit()  # salva as alterações no banco de dados
        print("Tabela criada com sucesso!")  # mensagem de sucesso
    except sqlite3.Error as erro:
        print("Erro ao criar a tabela:", erro)


def inserir_dados(conectar, cursor, nome_tabela, campos, dados):
    try:
        cursor.execute(  # executa um comando SQL
            f"""
                       INSERT INTO
                        {nome_tabela} {campos}
                       VALUES
                        ({','.join(['?'] * len(dados))});
                        """,
            dados,
        )
        conectar.commit()  # salva as alterações no banco de dados
        print("Dados inseridos com sucesso!")  # mensagem de sucesso
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados:", erro)


def inserir_muitos(conectar, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conectar.commit()  # salva as alterações no banco de dados


criar_tabela(
    conectar, cursor, "clientes", "id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(100), email varchar(150)"
)

inserir_dados(conectar, cursor, "clientes", "(nome, email)", ("João", "joao.jesus"))

muitos = [("Maria", "maria.silva"), ("José", "jose.santos")]
inserir_muitos(conectar, cursor, muitos)
