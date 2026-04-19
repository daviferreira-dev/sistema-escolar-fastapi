# 🏫 Sistema de Gestão Escolar API

Este projeto foi desenvolvido como parte da disciplina de **Banco de Dados** ministrada pelo **Prof. Anderson** na Faculdade Senai Felix Guisard. A API realiza a gestão completa de alunos, professores, cursos e matrículas, utilizando uma arquitetura moderna e escalável.

## 🚀 Tecnologias Utilizadas
- **Python & FastAPI**: Framework de alta performance para a construção da API.
- **SQLAlchemy**: ORM para mapeamento e manipulação do banco de dados relacional.
- **MySQL**: Banco de dados principal para armazenamento de dados estruturados.
- **MongoDB**: Banco de dados NoSQL utilizado para o Mural de Recados (Persistência Poliglota).
- **Pydantic**: Validação de dados e definição de Schemas.

## 🛠️ Funcionalidades
- CRUD completo de Alunos, Professores e Cursos.
- Sistema de Matrículas com relacionamentos complexos.
- Filtros dinâmicos (Alunos por cidade, Professores por região).
- Mural de recados flexível utilizando NoSQL.
- Documentação automática via Swagger UI.

## 📋 Como executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Configure as variáveis de ambiente no arquivo `.env`.
4. Inicie o servidor: `uvicorn main:app --reload`.
