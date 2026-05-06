from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models.product import Base
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Catálogo de Produtos",
    description=(
        "API REST para gerenciamento de catálogo de produtos.\n\n"
        "Suporta operações completas de CRUD com filtragem, paginação e busca."
    ),
    version="1.0.0",
    contact={"name": "Catálogo API"},
    license_info={"name": "MIT"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api")


@app.get("/api/health", tags=["Health"])
def health():
    return {"status": "ok", "service": "api-catalogo"}
