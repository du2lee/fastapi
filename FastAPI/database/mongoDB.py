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
    # tdd 시 connectMongo()가 시작되지 않아 아래 2줄 추가
    mongoAddress = 'mongodb://interx:interx%40504@server.interxlab.io:15115/admin'
    db.client = AsyncIOMotorClient(mongoAddress)
    return db.client


async def connectMongo():
    mongoAddress = os.getenv('MONGO_ADDRESS')
    db.client = AsyncIOMotorClient(mongoAddress)
    

async def disconnectMongo():
    if db.client:
        db.client.close()
    
