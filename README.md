# Finance Tracker API

API REST para controle financeiro pessoal desenvolvida com FastAPI.

O projeto tem foco em prática de backend, autenticação JWT, modelagem de banco de dados e arquitetura de APIs REST.

## Status

🚧 Em desenvolvimento

# Já implementado

* Estrutura organizada por domínio
* Configuração do PostgreSQL com SQLAlchemy
* Models relacionais (`User`, `Category`, `Transaction`)
* Migrations com Alembic
* Sistema de autenticação JWT
* Cadastro e login de usuários
* Hash de senha com bcrypt
* Rotas protegidas com `get_current_user`

---

# Funcionalidades planejadas

* CRUD de categorias
* CRUD de transações
* Filtros por categoria, período e tipo
* Resumo financeiro mensal
* Docker e Docker Compose
* Testes automatizados

---

# Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* python-jose
* passlib + bcrypt
* Docker *(planejado)*

---




 # Rodando o projeto

```bash id="h4gh7r"
# instalar dependências
pip install -r requirements.txt

# aplicar migrations
alembic upgrade head

# iniciar API
uvicorn app.main:app --reload
```

---

# Objetivo do projeto

Este projeto está sendo desenvolvido para aprofundar conhecimentos em:

* APIs REST
* Arquitetura backend
* SQLAlchemy
* Autenticação JWT
* Modelagem relacional
* Boas práticas com FastAPI
