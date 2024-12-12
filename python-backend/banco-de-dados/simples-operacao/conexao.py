import sqlite3
from pathlib import Path

# Conexão com o banco de dados
ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "database.db")  # conecta ao banco de dados
print("Conexão realizada com sucesso!")  # mensagem de sucesso

cursor = conexao.cursor()  # cria um cursor para manipular o banco de dados


def criar_tabela(conexao, cursor):
    cursor.execute(  # executa um comando SQL
        """
                   CREATE TABLE
                    IF NOT EXISTS
                    clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome varchar(100),
                        email varchar(150)
                    )
        """
    )
    conexao.commit()  # salva as alterações no banco de dados


def inserir_dados(conexao, cursor, nome, email):
    dados = (nome, email)
    cursor.execute(  # executa um comando SQL
        """
                   INSERT INTO
                    clientes (nome, email)
                   VALUES
                    (?,?);
                    """,
        dados,
    )
    conexao.commit()  # salva as alterações no banco de dados


def atualizar_dados(conexao, cursor, nome, email, id):
    dados = (nome, email, id)
    cursor.execute(  # executa um comando SQL
        """
                   UPDATE
                    clientes
                   SET
                  nome = ?,
                    email = ?
                   WHERE
                    id = ?;
        """,
        (dados),
    )
    conexao.commit()  # salva as alterações no banco de dados


def deletar_dados(conexao, cursor, id):
    cursor.execute(
        """
                   DELETE FROM
                    clientes
                   WHERE
                    id = ?;
        """,
        (id,),
    )
    conexao.commit()  # salva as alterações no banco de dados


#criar_tabela(conexao, cursor)

#inserir_dados(conexao, cursor, "João", "joao-j-v@hotmail.com")

#atualizar_dados(conexao, cursor, "João Vitor de Jesus Oliveira", "t_joao.jesus", 1)

deletar_dados(conexao, cursor, 3)
