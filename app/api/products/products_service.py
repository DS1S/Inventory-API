from typing import List, Union

from fastapi import HTTPException

import app.api as upper_service_functions

from app.db.mongo_driver import products_collection
from app.db.model_utils import PyObjectId

from app.api.products.product_models import ProductModel, \
    UpdateProductInfoModel, UpdateProductWarehouseModel


async def list_products_in_inventory():
    products = await products_collection.find().to_list(length=None)
    return products


async def create_product_in_inventory(product: ProductModel):
    new_product = await products_collection.insert_one(product)
    created_product = await products_collection.find_one(
        {"_id": new_product.inserted_id}
    )
    return created_product


async def update_product_in_inventory(
    request: Union[UpdateProductInfoModel, UpdateProductWarehouseModel],
    product_id: PyObjectId,
):
    if request.warehouse:
        if not (await upper_service_functions.verify_warehouse_id(
                request.warehouse
        )):
            raise HTTPException(
                status_code=400,
                detail="warehouse id is not a valid warehouse"
            )

    updated_product = await products_collection.find_one_and_update(
        {"_id": product_id},
        {"$set": request.dict(exclude_none=True)}
    )

    if updated_product:
        return updated_product

    raise HTTPException(
        status_code=404,
        detail=f"Product with id <{product_id}> not found"
    )


async def delete_product_in_inventory(product_id: PyObjectId):
    product_to_delete = await products_collection.find_one_and_delete(
        {"_id": product_id}
    )
    if product_to_delete:
        return product_to_delete

    raise HTTPException(
        status_code=404,
        detail=f"Product with id <{product_id}> not found"
    )


async def verify_products(product_ids: List[PyObjectId]):
    products_result = await products_collection.find(
        {"_id": {"$in": product_ids}}
    ).to_list(length=None)

    return len(product_ids) == len(products_result)


