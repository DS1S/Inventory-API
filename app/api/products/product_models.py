from typing import Optional

from pydantic import BaseModel, Field

from app.db.model_utils import PyObjectId, BaseConfig


class ProductModel(BaseModel):
    name: str = Field(...)
    price: int = Field(..., ge=0)  # Price is stored in cents
    supply: int = Field(..., ge=0)

    class Config(BaseConfig):
        schema_extra = {
            "example": {
                "name": "Can of Soup",
                "price": 231,
                "supply": 23,
            }
        }


class UpdateProductInfoModel(BaseModel):
    name: Optional[str] = Field(None)
    price: Optional[int] = Field(None, ge=0)
    supply: Optional[int] = Field(None, ge=0)


class UpdateProductWarehouseModel(UpdateProductInfoModel):
    warehouse: Optional[PyObjectId] = Field(None)


class ProductResponseModel(ProductModel):
    id: PyObjectId = Field(..., alias="_id")
    warehouse: Optional[PyObjectId] = Field(None)
