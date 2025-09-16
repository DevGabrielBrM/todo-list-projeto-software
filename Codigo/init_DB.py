import sqlite3
import os

# Caminho da pasta instance dentro da pasta do script
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# Caminho completo do banco
db_path = os.path.join(instance_path, 'tarefas.db')

# Cria banco e tabela tarefas
conn = sqlite3.connect(db_path)
conn.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
''')
conn.commit()
conn.close()

print("Banco de dados inicializado com sucesso!")
