#  Finance Tracker API

API REST para controle financeiro pessoal, construída com FastAPI.  
O projeto foca em consolidar conhecimentos em backend, modelagem de dados e autenticação, simulando um sistema real de gestão de gastos.




##  Status do projeto

🚧 Em desenvolvimento  
Atualmente implementado:
- Modelagem do banco de dados
- SQLAlchemy models
- Migrations com Alembic


##  Objetivo

Criar uma API onde o usuário pode:
- Se cadastrar e autenticar
- Gerenciar suas transações financeiras (receitas e despesas)
- Organizar gastos por categorias
- Consultar histórico e saldo

O foco principal não é UI, mas sim backend, arquitetura e boas práticas.



##  Funcionalidades planejadas

- Cadastro e login com JWT (access + refresh token)
- CRUD de transações (criar, listar, editar, deletar)
- Filtros por:
  - categoria
  - período (mês/ano)
  - tipo (receita/despesa)
- Resumo financeiro mensal (entradas, saídas e saldo)
- Isolamento de dados por usuário



##  Stack utilizada

- **FastAPI** — framework principal da API
- **Uvicorn** — servidor ASGI
- **PostgreSQL** — banco de dados relacional
- **SQLAlchemy** — ORM
- **Alembic** — migrations
- **python-jose** — autenticação JWT
- **passlib (bcrypt)** — hash de senhas
- **Docker & Docker Compose** — ambiente isolado e reproduzível



##  O que este projeto explora

- Autenticação JWT na prática (tokens, expiração, validação)
- Modelagem relacional com SQLAlchemy
- Relacionamentos entre entidades (User → Transactions → Categories)
- Migrations versionadas com Alembic
- Isolamento de dados por usuário
- Estrutura de API REST bem definida
- Ambiente replicável com Docker

