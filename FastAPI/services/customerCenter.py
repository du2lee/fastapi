import logging
import config as config
from models.customerCenter import *
from repo.baseRepo import *
from bson.objectid import ObjectId

logger = logging.getLogger(__name__)
collection = config.CUSTOMER_FAQ
collectionNotice = config.CUSTOMER_NOTICE

class FaqService:

    # 새로운 faq 추가
    async def addFaq(self, faqData: dict) -> dict:
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

    # 전체 faq 검색
    async def searchFaqs(self):
        faqs = []
        async for faq in find(config.DB_SELFLEARNING, collection):
            faqs.append(faq)
        return faqs

    # 해당 faq 검색
    async def searchFaq(self, id: str) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING,
            collection,
            {"_id": id})
        if faq:
            return faq

    # 해당 faq 수정
    async def updateFaq(self, id: str, data: dict) -> dict:
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
    async def deleteFaq(self, id: str) -> dict:
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

class NoticeService:

    # 새로운 notice 추가
    async def addNotice(self, noticeData: dict) -> dict:
        notice = await insert_one(
            config.DB_SELFLEARNING,
            collectionNotice,
            noticeData
        )

        newNotice = await find_one(
            config.DB_SELFLEARNING,
            collectionNotice,
            {"_id": notice.inserted_id})
        print(newNotice)
        return newNotice

    # 전체 notice 검색
    async def searchNotices(self):
        faqs = []
        async for faq in find(config.DB_SELFLEARNING, collectionNotice):
            faqs.append(faq)
        return faqs

    # 해당 notice 검색
    async def searchNotice(self, id: str) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING,
            collectionNotice,
            {"_id": id})
        if faq:
            return faq

    # 해당 notice 수정
    async def updateNotice(self, id: str, data: dict) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING, 
            collectionNotice,
            {"_id": id})
        copyData = data.copy()
        for key in data.keys():
            if data[key] == None:
                copyData.pop(key)
        if faq:
            await update_one(
                config.DB_SELFLEARNING, 
                collectionNotice, 
                {"_id": id},
                {"$set": copyData})
            
            faq = await find_one(
            config.DB_SELFLEARNING, 
            collectionNotice,
            {"_id": id})
            return faq

    # 해당 notice 삭제
    async def deleteNotice(self, id: str) -> dict:
        id = ObjectId(id)
        faq = await find_one(
            config.DB_SELFLEARNING, 
            collectionNotice,
            {"_id": id})
        if faq:
            await delete_one(
                config.DB_SELFLEARNING, 
                collectionNotice, 
                {"_id": id})
            return faq
