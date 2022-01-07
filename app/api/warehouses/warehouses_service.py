from fastapi import HTTPException
from pymongo import ReturnDocument

from app.db.mongo_driver import warehouse_collection
from app.db.model_utils import PyObjectId

import app.api as upper_level_services
from app.api.products.product_models import UpdateProductWarehouseModel
from app.api.warehouses.warehouses_models import \
    WarehouseProductUpdateRequestModel


async def get_all_warehouses_in_collection():
    return await warehouse_collection.find().to_list(length=None)


async def create_warehouse_in_collection(warehouse):
    warehouse["inventory"] = []
    new_warehouse = await warehouse_collection.insert_one(warehouse)
    created_warehouse = await warehouse_collection.find_one(
        {"_id": new_warehouse.inserted_id}
    )
    return created_warehouse


async def verify_warehouse_id(warehouse_id):
    return bool(await warehouse_collection.find_one({"_id": warehouse_id}))


async def add_product_to_warehouse_in_collection(
        request: WarehouseProductUpdateRequestModel,
        warehouse_id: PyObjectId
):
    request.new_products = list(set(request.new_products))

    if not upper_level_services.verify_products(request.new_products):
        raise HTTPException(
            status_code=400,
            detail="Some or all object ids in request are not product ids"
        )

    warehouse = await warehouse_collection.find_one({"_id": warehouse_id})

    if warehouse["inventory"]:
        request.new_products = list(
            set(warehouse["inventory"]).difference(request.new_products)
        )

    if not request.new_products:
        return warehouse

    product_update_request = UpdateProductWarehouseModel(
        warehouse=warehouse_id
    )

    for product_id in request.new_products:
        await upper_level_services.update_product_in_inventory(
            product_update_request,
            product_id
        )

    return await warehouse_collection.find_one_and_update(
        {"_id": warehouse_id},
        {"$push": {"inventory": {"$each": request.new_products}}},
        return_document=ReturnDocument.AFTER
    )
