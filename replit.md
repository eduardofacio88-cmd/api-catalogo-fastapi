# API Catálogo de Produtos (FastAPI)

Uma API REST em Python/FastAPI para gerenciamento completo de catálogo de produtos, com CRUD, paginação, filtros e Swagger UI integrada.

## Run & Operate

- `bash artifacts/catalogo-api/run.sh` — start the FastAPI catalog API (port 8000)
- `python artifacts/catalogo-api/seed.py` — seed the DB with 10 sample products (auto-runs on start)
- Workflow: `Catálogo API (FastAPI)` — runs the FastAPI server
- Docs: `http://localhost:8000/docs` — Swagger UI (interactive)
- Docs: `http://localhost:8000/redoc` — ReDoc

## Stack

- Python 3.11, FastAPI, Uvicorn
- SQLAlchemy ORM (SQLite for dev, Postgres in prod via `DATABASE_URL`)
- Pydantic v2 for request/response validation
- Also in workspace: Node.js 24 / Express 5 api-server (separate artifact, port 8080, path `/api`)

## Where things live

```
artifacts/catalogo-api/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # SQLAlchemy engine + session
│   ├── schemas.py       # Pydantic request/response models
│   ├── models/
│   │   └── product.py   # SQLAlchemy Product model
│   └── routers/
│       └── products.py  # All CRUD + filter routes
├── seed.py              # Sample data seeder (10 products)
├── run.sh               # Startup script (seed + uvicorn)
└── requirements.txt     # Python dependencies
```

## Architecture decisions

- SQLite by default for zero-config local dev; switches to Postgres automatically when `DATABASE_URL` env var is set (used in prod).
- `redirect_slashes=False` on FastAPI to avoid 307 redirects on routes without trailing slash.
- All routes prefixed with `/api` inside the app; the router uses `/products` prefix.
- Seed runs on every startup but is a no-op if products already exist.
- psycopg2-binary installed for Postgres support in production.

## Product

- `GET /api/products/` — list products with pagination, search, category filter, price range, in-stock filter
- `POST /api/products` — create a product (validates SKU uniqueness)
- `GET /api/products/{id}` — get product by ID
- `PUT /api/products/{id}` — update product fields (partial updates supported)
- `DELETE /api/products/{id}` — delete product
- `GET /api/products/categories` — list distinct categories
- `GET /api/health` — health check
- `GET /docs` — Swagger UI

## User preferences

- Python + FastAPI (explicitly requested over Node.js)
- Full CRUD on product catalog (name, price, category, stock, SKU, description)

## Gotchas

- Always use trailing slash on list endpoints: `/api/products/` not `/api/products`
- The existing `artifacts/api-server` occupies `/api` in the reverse proxy; the FastAPI app runs on port 8000 directly (not proxied through the shared proxy)
- `pnpm run typecheck` only covers the Node.js workspace packages, not the Python app

## Pointers

- See the `pnpm-workspace` skill for workspace structure details
- FastAPI docs: https://fastapi.tiangolo.com
