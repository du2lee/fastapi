import logging
import config as config
from models.customerCenter import *
from repo.baseRepo import *
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)
collection = config.CUSTOMER_FAQ

class FaqService:

    # 새로운 faq 추가
    async def addFaq(faqData: dict) -> dict:
        faq = await insert_one(
            config.DB_SELFLEARNING,
            collection,
            faqData
        )

        newFaq = await find_one(
            config.DB_SELFLEARNING,
            collection,
            {"_id": faq.inserted_id})
        return newFaq

    # 전체 payments 검색
    async def searchFaqs():
        faqs = []
        async for faq in find(config.DB_SELFLEARNING, collection):
            faqs.append(faq)
        return faqs

    # 해당 faq 검색
    async def searchFaq(id: str) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING,
            collection,
            {"_id": id})
        if faq:
            return faq

    # 해당 faq 수정
    async def updateFaq(id: str, data: dict) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING, 
            collection,
            {"_id": id})
        copyData = data.copy()
        for key in data.keys():
            if data[key] == None:
                copyData.pop(key)
        if faq:
            await update_one(
                config.DB_SELFLEARNING, 
                collection, 
                {"_id": id},
                {"$set": copyData})
            
            faq = await find_one(
            config.DB_SELFLEARNING, 
            collection,
            {"_id": id})
            return faq

    # 해당 faq 삭제
    async def deleteFaq(id: str) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING, 
            collection,
            {"_id": id})
        if faq:
            await delete_one(
                config.DB_SELFLEARNING, 
                collection, 
                {"_id": id})
            return faq
