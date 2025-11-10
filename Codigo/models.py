from database import get_db

def listar_tarefas():
    db = get_db()
    return db.execute('SELECT * FROM tarefas').fetchall()

def adicionar_tarefa(nome):
    db = get_db()
    db.execute('INSERT INTO tarefas (nome, status) VALUES (?, "PENDENTE")', (nome,))
    db.commit()

def concluir_tarefa(id):
    db = get_db()
    db.execute('UPDATE tarefas SET status = "CONCLUIDA" WHERE id = ?', (id,))
    db.commit()

def editar_tarefa(id, novo_nome):
    db = get_db()
    db.execute('UPDATE tarefas SET nome = ? WHERE id = ?', (novo_nome, id))
    db.commit()

def excluir_tarefa(id):
    db = get_db()
    db.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    db.commit()
