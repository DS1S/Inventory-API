from typing import List

from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder

from app.db.model_utils import PyObjectId

from app.api.warehouses.warehouses_models import WarehouseModel, \
    WarehouseResponseModel, WarehouseProductUpdateRequestModel
from app.api.warehouses.warehouses_service import \
    get_all_warehouses_in_collection, \
    create_warehouse_in_collection, \
    add_product_to_warehouse_in_collection

warehouse_router = APIRouter()


@warehouse_router.get("/", response_model=List[WarehouseResponseModel])
async def list_warehouses():
    return await get_all_warehouses_in_collection()


@warehouse_router.post("/", response_model=WarehouseResponseModel)
async def create_warehouse(request: WarehouseModel):
    return await create_warehouse_in_collection(jsonable_encoder(request))


@warehouse_router.post("/{warehouseId}", response_model=WarehouseResponseModel)
async def add_product_to_warehouse(
        request: WarehouseProductUpdateRequestModel,
        warehouse_id: PyObjectId = Path(..., alias="warehouseId")
):
    return await add_product_to_warehouse_in_collection(request, warehouse_id)


