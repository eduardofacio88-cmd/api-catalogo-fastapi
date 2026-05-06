"""Seed script — populates the database with sample products."""
from app.database import SessionLocal, engine
from app.models.product import Base, Product

Base.metadata.create_all(bind=engine)

PRODUCTS = [
    {"name": "Camiseta Básica", "description": "Camiseta 100% algodão, disponível em várias cores", "price": 39.90, "category": "Roupas", "stock": 150, "sku": "CAM-BASIC-001"},
    {"name": "Calça Jeans Slim", "description": "Calça jeans slim fit com elastano", "price": 129.90, "category": "Roupas", "stock": 80, "sku": "CAL-JEANS-002"},
    {"name": "Tênis Running Pro", "description": "Tênis para corrida com amortecimento avançado", "price": 299.90, "category": "Calçados", "stock": 45, "sku": "TEN-RUN-003"},
    {"name": "Mochila Urbana 20L", "description": "Mochila impermeável com compartimento para notebook", "price": 189.90, "category": "Acessórios", "stock": 60, "sku": "MOC-URB-004"},
    {"name": "Relógio Digital Sport", "description": "Relógio esportivo à prova d'água 50m", "price": 249.90, "category": "Acessórios", "stock": 30, "sku": "REL-DIG-005"},
    {"name": "Notebook Gamer 15'", "description": "Notebook com GPU dedicada e 16GB RAM", "price": 4999.90, "category": "Eletrônicos", "stock": 10, "sku": "NOT-GAM-006"},
    {"name": "Fone Bluetooth ANC", "description": "Fone com cancelamento de ruído ativo", "price": 599.90, "category": "Eletrônicos", "stock": 25, "sku": "FON-BLU-007"},
    {"name": "Cadeira Ergonômica", "description": "Cadeira de escritório com suporte lombar ajustável", "price": 899.90, "category": "Móveis", "stock": 15, "sku": "CAD-ERG-008"},
    {"name": "Suplemento Whey Protein 1kg", "description": "Proteína do soro do leite, sabor chocolate", "price": 99.90, "category": "Suplementos", "stock": 200, "sku": "SUP-WHE-009"},
    {"name": "Garrafa Térmica 1L", "description": "Mantém bebidas quentes/frias por 12h", "price": 59.90, "category": "Acessórios", "stock": 0, "sku": "GAR-TER-010"},
]


def seed():
    db = SessionLocal()
    try:
        existing = db.query(Product).count()
        if existing > 0:
            print(f"Database already has {existing} products. Skipping seed.")
            return
        for data in PRODUCTS:
            db.add(Product(**data))
        db.commit()
        print(f"Seeded {len(PRODUCTS)} products successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
