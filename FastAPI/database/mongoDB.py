from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import logging, os

__all__ = ["getConnection", "connectMongo", "disconnectMongo"]

logger = logging.getLogger(__name__)
load_dotenv(verbose=True)


class MongoDataBase:
    client: AsyncIOMotorClient = None


db = MongoDataBase()


def getConnection() -> AsyncIOMotorClient:
    return db.client


async def connectMongo():
    mongoAddress = os.getenv('MONGO_ADDRESS')
    db.client = AsyncIOMotorClient(mongoAddress)
    

async def disconnectMongo():
    if db.client:
        db.client.close()
    
