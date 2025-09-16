# todo-list-projeto-software
Projeto desenvolvido para a disciplina de Projeto de Software, contendo front-end, back-end e banco de dados, assim como documentos adicionais.

Perfeito! 🚀 Podemos criar um **README.md inicial** bem profissional, explicando até onde chegamos e já preparando terreno para as próximas sprints. Aqui vai uma sugestão para o seu projeto:

---

```markdown
# 🧑‍💻 Projeto de Software – Sistema de Tarefas

Este repositório contém o desenvolvimento do projeto para a disciplina **Projeto de Software**, seguindo o modelo de desenvolvimento em camadas **(Front-end, Back-end e Banco de Dados)**.  
O projeto será entregue em **4 sprints**, e este repositório documenta o progresso desde a Sprint 1.

---

## 📌 Sprint 1 – Estrutura Inicial do Projeto ✅

Nesta primeira sprint, focamos em **organizar a base do projeto** e preparar o ambiente para desenvolvimento.  

### 🏗️ Estrutura de Pastas Criada
```

Projeto\_Software/
│   README.md
│
├───Board/              # Planejamento (Kanban, ideias, requisitos)
├───Codigo/             # Código-fonte principal
│   │   app.py          # Arquivo principal (Flask)
│   │   database.py     # Conexão com o banco de dados
│   │   init\_DB.py      # Script para inicialização do banco
│   │   models.py       # Modelos e funções de acesso ao banco
│   │
│   ├───static/         # Arquivos estáticos (CSS, JS, imagens)
│   └───templates/      # Templates HTML (Jinja2)
│
├───Documentacao/       # Documentos do projeto (PDFs, diagramas)
└───Videos/             # Vídeos de apresentação

````

### 🗄️ Banco de Dados
- Criada a pasta `instance/` para armazenar o banco SQLite.
- Criado o banco `tarefas.db` com a tabela inicial:
```sql
CREATE TABLE tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
);
````

### 🌐 Back-End

* Implementação do `app.py` com Flask.
* Configuração inicial de rota `/` para listar tarefas.

### 🎨 Front-End

* Criado `templates/index.html` com um layout simples para exibir tarefas.
* Criado `static/style.css` para estilos básicos.

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Entre na pasta de código:

```bash
cd Codigo
```

3. Crie o banco de dados:

```bash
python init_DB.py
```

4. Rode o servidor Flask:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 📅 Próximas Sprints

* **Sprint 2:** Criar rotas para adicionar e remover tarefas.
* **Sprint 3:** Melhorar layout e implementar edição de tarefas.
* **Sprint 4:** Testes, documentação final e deploy.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Framework Web:** Flask
* **Banco de Dados:** SQLite
* **Front-End:** HTML + CSS (Jinja2 Templates)
* **Controle de Versão:** Git & GitHub

---

## 👤 Autor

**Gabriel Briotto Monteiro**
Projeto desenvolvido para a disciplina **Projeto de Software**.

```

---

Quer que eu já adicione esse README.md no seu projeto (dentro da raiz, onde está a pasta `Board`, `Codigo`, etc.) e te mostre os comandos Git para versionar e mandar para o GitHub?
```
