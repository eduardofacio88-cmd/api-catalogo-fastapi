from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Catálogo de Mercado 🛒")

# 1. Definimos o modelo do produto (o esqueleto)
class Produto(BaseModel):
    nome: str
    preco: float
    categoria: str
    marca: str

# Banco de dados temporário em memória (uma lista Python)
banco_produtos: List[Produto] = []

# 2. Rota para cadastrar um novo produto (POST)
@app.post("/produtos", response_model=Produto)
def cadastrar_produto(produto: Produto):
    banco_produtos.append(produto)
    return produto

# 3. Rota para listar todos os produtos cadastrados (GET)
@app.get("/produtos", response_model=List[Produto])
def listar_produtos():
    return banco_produtos
