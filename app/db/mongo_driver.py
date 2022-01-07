import motor.motor_asyncio
from app.settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
db = client.inventory

products_collection = db.get_collection("products")
warehouse_collection = db.get_collection("warehouses")
