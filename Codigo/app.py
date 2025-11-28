from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

DB_PATH = os.path.join(BASE_DIR, 'instance', 'tarefas.db')

def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = conectar()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            status TEXT DEFAULT 'PENDENTE'
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = conectar()
    tarefas = conn.execute('SELECT * FROM tarefas').fetchall()
    conn.close()
    return render_template('index.html', tarefas=tarefas)

@app.route('/add', methods=['POST'])
def add_tarefa():
    nome = request.form['nome']
    if nome.strip():
        conn = conectar()
        conn.execute('INSERT INTO tarefas (nome) VALUES (?)', (nome,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/tarefas/<int:id>/concluir', methods=['POST'])
def concluir(id):
    conn = conectar()
    conn.execute('UPDATE tarefas SET status = ? WHERE id = ?', ('CONCLUIDA', id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/tarefas/<int:id>', methods=['POST'])
def editar(id):
    novo_nome = request.form['novo_nome']
    if novo_nome.strip():
        conn = conectar()
        conn.execute('UPDATE tarefas SET nome = ? WHERE id = ?', (novo_nome, id))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/tarefas/<int:id>/excluir', methods=['POST'])
def excluir_tarefa_route(id):
    conn = conectar()
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# --- NOVAS ROTAS DA SPRINT 4 ---

@app.route('/relatorio')
def relatorio_json():
    """Retorna os dados em formato JSON para o gráfico"""
    conn = conectar()
    total = conn.execute('SELECT COUNT(*) FROM tarefas').fetchone()[0]
    concluidas = conn.execute('SELECT COUNT(*) FROM tarefas WHERE status = "CONCLUIDA"').fetchone()[0]
    pendentes = conn.execute('SELECT COUNT(*) FROM tarefas WHERE status = "PENDENTE"').fetchone()[0]
    conn.close()
    
    return jsonify({
        'total': total,
        'concluidas': concluidas,
        'pendentes': pendentes
    })

@app.route('/estatisticas')
def pagina_relatorio():
    """Renderiza a página HTML do relatório"""
    return render_template('relatorio.html')

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)