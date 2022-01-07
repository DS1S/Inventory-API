from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import settings

from app.api.health.health_controller import health_router
from app.api.products.products_controller import products_router
from app.api.warehouses.warehouses_controller import warehouse_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(health_router, tags=["Health"])
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(warehouse_router, prefix="/warehouses", tags=["Warehouses"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)
