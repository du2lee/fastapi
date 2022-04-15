from motor.motor_asyncio import AsyncIOMotorClient
import logging

__all__ = ["getConnection", "connectMongo", "disconnectMongo"]

logger = logging.getLogger(__name__)


class MongoDataBase:
    client: AsyncIOMotorClient = None


db = MongoDataBase()


def getConnection() -> AsyncIOMotorClient:
    return db.client


async def connectMongo():
    mongoAddress = "mongodb://interx:interx%40504@{0}/admin".format("server.interxlab.io:15115")
    db.client = AsyncIOMotorClient(mongoAddress)
    

async def disconnectMongo():
    if db.client:
        db.client.close()
    
