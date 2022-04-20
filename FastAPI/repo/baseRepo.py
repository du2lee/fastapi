from database.mongoDB import *

"""
In vscode, AsyncIOMotorClient intelisense not works.
so wrappping it with custom method
"""

__all__ = ["insert_one", "find", "find_one", "update_one", "delete_one"]


async def insert_one(database: str, collection: str, param: dict):
    return await getConnection()[database][collection].insert_one(param)


def find(database: str, collection: str):
    return getConnection()[database][collection].find()


async def find_one(database: str, collection: str, param: dict):
    return await getConnection()[database][collection].find_one(param)


async def update_one(database: str, collection: str, param: dict, param2: dict):
    return await getConnection()[database][collection].update_one(param, param2)


async def delete_one(database: str, collection: str, param: dict):
    return await getConnection()[database][collection].delete_one(param)