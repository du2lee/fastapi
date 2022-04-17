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
    # mongoAddress = "mongodb://interx:interx%40504@{0}/admin".format("server.interxlab.io:15115")
    mongoAddress = os.environ.get('MONGO_ADDRESS')
    db.client = AsyncIOMotorClient(mongoAddress)
    

async def disconnectMongo():
    if db.client:
        db.client.close()
    
