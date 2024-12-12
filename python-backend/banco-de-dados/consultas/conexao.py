import sqlite3
from pathlib import Path

# Conexão com o banco de dados
ROOT_PATH = Path(__file__).parent

try:
    conectar = sqlite3.connect(ROOT_PATH / "database.db")  # conecta ao banco de dados
    print("Conexão realizada com sucesso!")  # mensagem de sucesso
    cursor = conectar.cursor()  # cria um cursor para manipular o banco de dados
    print("Cursor criado com sucesso!")  # mensagem de sucesso
    cursor.row_factory = sqlite3.Row
    print("Row factory configurado com sucesso!")  # mensagem de sucesso
except sqlite3.Error as erro:
    print("Erro ao conectar ao banco de dados:", erro)


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
    try:
        cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
        conectar.commit()  # salva as alterações no banco de dados
        print("Múltiplos dados inseridos com sucesso!")  # mensagem de sucesso
    except sqlite3.Error as erro:
        print("Erro ao inserir os dados:", erro)


def buscar_dado(conectar, cursor, nome_tabela, campos, condicao):
    try:
        cursor.execute(f"SELECT {campos} FROM {nome_tabela} WHERE {condicao}")
        resultado = cursor.fetchone()
        print(resultado)
    except sqlite3.Error as erro:
        print("Erro ao buscar os dados:", erro)


def buscar_dados(conectar, cursor, nome_tabela, campos, condicao):
    try:
        cursor.execute(f"SELECT {campos} FROM {nome_tabela} WHERE {condicao}")
        resultado = cursor.fetchall()
        print(resultado)
    except sqlite3.Error as erro:
        print("Erro ao buscar os dados:", erro)


def recuperar_cliente(cursor, nome_tabela, campos, condicao):
    try:
        return cursor.execute(f"SELECT {campos} FROM {nome_tabela} {condicao}").fetchone()
    except sqlite3.Error as erro:
        print("Erro ao buscar os dados:", erro)


def listar_clientes(cursor, nome_tabela, campos, condicao):
    try:
        return cursor.execute(f"SELECT {campos} FROM {nome_tabela} {condicao}").fetchall()
    except sqlite3.Error as erro:
        print("Erro ao buscar os dados:", erro)


# criar_tabela(conectar, cursor, "clientes", "id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(100), email varchar(150)")

# inserir_dados(conectar, cursor, "clientes", "(nome, email)", ("João", "joao.jesus"))

muitos = [
    ("Maria", "maria.silva"),
    ("José", "jose.santos"),
    ("Ana", "ana.santos"),
    ("Carlos", "carlos.martins"),
    ("Fernanda", "fernanda.oliveira"),
    ("Lucas", "lucas.martins"),
    ("Patrícia", "patricia.silva"),
    ("Rafael", "rafael.almeida"),
    ("Juliana", "juliana.oliveira"),
    ("Mateus", "mateus.souza"),
    ("Larissa", "larissa.pereira"),
    ("Tiago", "tiago.rodrigues"),
    ("Vanessa", "vanessa.mendes"),
    ("Pedro", "pedro.gomes"),
    ("Mariana", "mariana.costa"),
    ("Thiago", "thiago.souza"),
    ("Renata", "renata.alves"),
    ("Gabriel", "gabriel.lima"),
    ("Julio", "julio.pinto"),
    ("Beatriz", "beatriz.fernandes"),
]

# inserir_muitos(conectar, cursor, muitos)

# buscar_dado(conectar, cursor, "clientes", "id", "nome = 'João'")

# buscar_dados(conectar, cursor, "clientes", "*", "nome = 'João'")

print("\nCliente recuperado:")
cliente = recuperar_cliente(cursor, "clientes", "*", "WHERE nome = 'João'")
print(dict(cliente))
print(cliente["nome"])

print("\nLista de clientes:")
clientes = listar_clientes(cursor, "clientes", "*", "ORDER BY id ASC")
for c in clientes:
    print(dict(c)["nome"])
#    print(c["nome"])
