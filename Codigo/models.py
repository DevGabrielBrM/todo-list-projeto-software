from database import get_db

def listar_tarefas():
    db = get_db()
    return db.execute('SELECT * FROM tarefas').fetchall()

def adicionar_tarefa(nome):
    db = get_db()
    db.execute('INSERT INTO tarefas (nome) VALUES (?)', (nome,))
    db.commit()