from typing import List

from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder

from app.db.model_utils import PyObjectId
from app.api.products.products_service import list_products_in_inventory, \
    create_product_in_inventory, delete_product_in_inventory, \
    update_product_in_inventory
from app.api.products.product_models import ProductModel, \
    ProductResponseModel, \
    UpdateProductInfoModel

products_router = APIRouter()


@products_router.get("/", response_model=List[ProductResponseModel])
async def view_products():
    return await list_products_in_inventory()


@products_router.post("/", response_model=ProductResponseModel)
async def create_product(product: ProductModel):
    product = jsonable_encoder(product)
    created_product = await create_product_in_inventory(product)
    return created_product


@products_router.delete("/{productId}", response_model=ProductResponseModel)
async def delete_product(product_id: PyObjectId = Path(..., alias="productId")):
    deleted_product = await delete_product_in_inventory(product_id)
    return deleted_product


@products_router.patch("/{productId}", response_model=ProductResponseModel)
async def update_product(
    request: UpdateProductInfoModel,
    product_id: PyObjectId = Path(..., alias="productId")
):
    updated_product = await update_product_in_inventory(request, product_id)
    return updated_product

