🧑‍💻 Projeto de Software – Sistema de Tarefas

Este repositório contém o desenvolvimento do projeto para a disciplina Projeto de Software, seguindo o modelo de desenvolvimento em camadas (Front-end, Back-end e Banco de Dados).

O projeto foi entregue em 4 sprints, e este repositório documenta a versão final.

📌 Status do Projeto: CONCLUÍDO ✅

Todas as funcionalidades planejadas foram implementadas com sucesso.

🏗️ Estrutura de Pastas Final

Projeto_Software/
│   README.md
│
├───Codigo/             # Código-fonte principal
│   │   app.py          # Arquivo principal (Flask com Rotas API e View)
│   │   database.py     # Conexão com o banco de dados
│   │   init_DB.py      # Script para inicialização do banco
│   │   models.py       # Modelos de dados
│   │
│   ├───static/         # Arquivos estáticos (style.css)
│   └───templates/      # Templates HTML
│       │   index.html      # Página principal
│       │   relatorio.html  # Página de dashboard (Novo!)


✨ Funcionalidades Implementadas

Gerenciamento de Tarefas (CRUD):

Listar todas as tarefas.

Adicionar novas tarefas.

Editar tarefas existentes (via Modal).

Excluir tarefas.

Marcar tarefas como CONCLUÍDA.

Dashboard e Relatórios (Sprint 4):

Rota /relatorio retornando JSON com contagem de status.

Página /estatisticas com gráfico de rosca (Chart.js) mostrando visualmente a produtividade.

📅 Histórico de Sprints

Sprint 1: Estrutura inicial, Banco de Dados e Listagem. ✅

Sprint 2: Rotas para Adicionar e Excluir tarefas. ✅

Sprint 3: Melhoria de Layout e Edição de tarefas. ✅

Sprint 4: Relatórios, Gráficos e Documentação Final. ✅

🚀 Como Rodar o Projeto

Clone o repositório e entre na pasta Codigo.

Instale as dependências (se necessário):

pip install flask


Inicialize o banco de dados:

python init_DB.py


Rode o servidor:

python app.py


Acesse no navegador:

Lista: http://127.0.0.1:5000

Relatório: http://127.0.0.1:5000/estatisticas

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.13

Framework Web: Flask

Banco de Dados: SQLite

Front-End: HTML5, CSS3, JavaScript (Fetch API + Chart.js)

👤 Autor

Gabriel Briotto Monteiro
Projeto desenvolvido para a disciplina Projeto de Software.