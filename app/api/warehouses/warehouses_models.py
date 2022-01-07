from typing import List
from pydantic import BaseModel, Field
from app.db.model_utils import PyObjectId, BaseConfig


class WarehouseModel(BaseModel):
    name: str = Field(...)
    location: str = Field(...)
    lat: float = Field(..., ge=-90, le=90)
    long: float = Field(..., ge=-180, le=180)

    class Config(BaseConfig):
        schema_extra = {
            "example": {
                "name": "Vaughn Mills & CO",
                "location": "Toronto - Vaughn Mills",
                "lat": 32.231,
                "long": 123.12,
            }
        }


class WarehouseProductUpdateRequestModel(BaseModel):
    new_products: List[PyObjectId] = Field(...)


class WarehouseResponseModel(WarehouseModel):
    id: PyObjectId = Field(..., alias="_id")
    inventory: List[PyObjectId] = Field(...)
