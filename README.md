 # 📦 API de Catálogo de Produtos

 Esta é uma API REST simples desenvolvida em **Python** utilizando o framework **FastAPI**. O projeto permite gerenciar um catálogo de produtos com operações completas de CRUD (Criar, Ler, Atualizar e Deletar).

 ## 🚀 Funcionalidades

 * 🔍 **Listar e Filtrar**: Retorna os produtos cadastrados.
 * ➕ **Cadastro de Itens**: Permite adicionar novos produtos ao catálogo.
 * 🛠️ **CRUD Completo**: Atualização e remoção de produtos de forma simples.
 * 📖 **Documentação Interativa**: Interface gráfica integrada via Swagger UI.

 ## 💻 Como Rodar o Projeto Localmente

  ### 1. Clonar o repositório
 ```bash
 git clone https://github.com/eduardofacio88-cmd/api-catalogo-fastapi.git
 cd api-catalogo-fastapi
 pip install fastapi uvicorn
 uvicorn main:app --reload

 