from database import get_db, close_db
from flask import Flask, render_template, request, redirect, g
from models import listar_tarefas, adicionar_tarefa

app = Flask(__name__)
app.teardown_appcontext(close_db)


@app.route('/')
def index():
    tarefas = listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    adicionar_tarefa(nome)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)