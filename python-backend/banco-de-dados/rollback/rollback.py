import sqlite3
from pathlib import Path

# Conexão com o banco de dados
ROOT_PATH = Path(__file__).parent

try:
    conexao = sqlite3.connect(ROOT_PATH / 'database.db')
    cursor = conexao.cursor()
    cursor.row_factory = sqlite3.Row
    print('Conectado ao banco de dados')
    print('Conexão com o banco de dados')
    print('Cursor criado com sucesso')
except sqlite3.Error as erro:
    print('Erro ao conectar com o banco de dados:', erro)
    conexao.close()

# Inserindo dados na tabela
try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES ("deu-rollback3", "deu-rollback@email.com")')
    print('Dados inseridos com sucesso')
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (30, "deu-rollback-4", "deu-rollback2@email.com"')
    print('Dados inseridos com sucesso')
    conexao.commit()
except Exception as exc:
    print('Erro ao inserir dados:', exc)
    conexao.rollback()
    print('Rollback executado com sucesso')
finally:
    conexao.close()
    print('Conexão com o banco de dados fechada')
