import sqlite3
import os

# Caminho da pasta instance dentro da pasta do script
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# Caminho completo do banco
db_path = os.path.join(instance_path, 'tarefas.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Cria a tabela JÁ COM A COLUNA STATUS se ela não existir.
#    Isso resolve o erro para bancos de dados novos.
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'PENDENTE'
)
''')

# 2. Tenta adicionar a coluna 'status' para garantir a migração de bancos antigos.
#    Se a coluna já existir (pelo CREATE acima ou por uma execução anterior),
#    o try/except evitará um erro.
try:
    cursor.execute('ALTER TABLE tarefas ADD COLUMN status TEXT NOT NULL DEFAULT "PENDENTE"')
    print("Migração: Coluna 'status' adicionada com sucesso!")
except sqlite3.OperationalError as e:
    # A gente espera o erro "duplicate column name" se a coluna já existe.
    if "duplicate column name: status" in str(e):
        print("Info: Coluna 'status' já existe.")
    else:
        # Se for outro erro, aí sim queremos que ele apareça.
        raise e

# 3. Garante que qualquer tarefa antiga que possa ter ficado com status NULO seja atualizada.
cursor.execute("UPDATE tarefas SET status = 'PENDENTE' WHERE status IS NULL")

conn.commit()
conn.close()

print("Banco de dados inicializado/migrado com sucesso!")