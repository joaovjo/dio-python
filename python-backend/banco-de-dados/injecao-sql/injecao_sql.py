import sqlite3
from pathlib import Path

# Conexão com o banco de dados

ROOT_PATH = Path(__file__).parent

try:
    conectar = sqlite3.connect(ROOT_PATH / 'database.db')
    print('Conectado com sucesso!')
    cursor = conectar.cursor()
    print('Cursor criado com sucesso!')
    cursor.row_factory = sqlite3.Row
    print('Row factory criado com sucesso!')
except sqlite3.Error as erro:
    print('Erro ao conectar com o banco de dados:', erro)

id_cliente = input('Digite o ID do cliente: ')
# cliente = cursor.execute(f'SELECT * FROM clientes WHERE id = {id_cliente}').fetchone()
# print(dict(cliente))

clientes = cursor.execute(f'SELECT * FROM clientes WHERE id = {id_cliente}').fetchall()
for cliente in clientes:
    print(dict(cliente))