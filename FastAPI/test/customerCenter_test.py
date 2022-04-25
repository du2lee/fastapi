import os, pytest, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from httpx import AsyncClient
from bson.objectid import ObjectId
from app import app

baseUrl = "http://test"

@pytest.mark.asyncio
async def test_postFaq():
    global faqId, time
    async with AsyncClient(app = app, base_url = baseUrl) as client:
        response = await client.post("/api-customercenter/faq", 
        json={
                "category" : "중요!!",
                "title" : "문의사항",
                "content" : "I wanna go home",
            })
        faqId = response.json()['_id']
        time = response.json()['created_at']

        assert response.status_code == 201

@pytest.mark.asyncio
async def test_getFaq():
    async with AsyncClient(app = app, base_url = baseUrl) as client:
        response = await client.get("/api-customercenter/faq", params={"id": ObjectId(faqId)})

        assert response.status_code == 200
        assert response.json() == {
                "_id": faqId,
                "created_at": time,
                "category": "중요!!",
                "title": "문의사항",
                "content": "I wanna go home"
        }

@pytest.mark.asyncio
async def test_getFaqs():
    async with AsyncClient(app = app, base_url = baseUrl) as client:
        
        response = await client.get("/api-customercenter/faqs")

        assert response.status_code == 200

@pytest.mark.asyncio
async def test_updateFaq():
    global faqId, time
    async with AsyncClient(app = app ,base_url = baseUrl) as client:
        response = await client.patch("/api-customercenter/faq", params={"id": ObjectId(faqId)},
        json={
                "category" : "잡담",
            })
        faqId = response.json()['_id']
        time = response.json()['created_at']

        assert response.status_code == 200
        assert response.json() == {
                "_id": faqId,
                "created_at": time,
                "category": "잡담",
                "title": "문의사항",
                "content": "I wanna go home"
        }

@pytest.mark.asyncio
async def test_deleteFaq():
    async with AsyncClient(app = app ,base_url = baseUrl) as client:
        response = await client.delete("/api-customercenter/faq", params={"id": ObjectId(faqId)})

        assert response.status_code == 200
        assert response.json() == {
                "_id": faqId,
                "created_at": time,
                "category": "잡담",
                "title": "문의사항",
                "content": "I wanna go home"
        }



# ================================================================================

@pytest.mark.asyncio
async def test_postNotice():
    global noticeId, time
    async with AsyncClient(app = app, base_url = baseUrl) as client:
        response = await client.post("/api-customercenter/notice", 
        json={
                "title" : "문의사항",
                "content" : "I wanna go home",
            })
        noticeId = response.json()['_id']
        time = response.json()['date']

        assert response.status_code == 201

@pytest.mark.asyncio
async def test_getNotice():
    async with AsyncClient(app = app, base_url = baseUrl) as client:
        response = await client.get("/api-customercenter/notice", params={"id": ObjectId(noticeId)})

        assert response.status_code == 200
        # assert response.json() == {
        #         "_id": noticeId,
        #         "date": time,
        #         "title": "문의사항",
        #         "content": "I wanna go home"
        # }

@pytest.mark.asyncio
async def test_getNotices():
    async with AsyncClient(app = app, base_url = baseUrl) as client:
        
        response = await client.get("/api-customercenter/notices")

        assert response.status_code == 200

@pytest.mark.asyncio
async def test_updateNotice():
    global noticeId, time
    async with AsyncClient(app = app ,base_url = baseUrl) as client:
        response = await client.patch("/api-customercenter/notice", params={"id": ObjectId(noticeId)},
        json={
                "content" : "I am in my house"
            })
        noticeId = response.json()['_id']
        time = response.json()['date']

        assert response.status_code == 200
        # assert response.json() == {
        #         "_id": noticeId,
        #         "date": time,
        #         "title": "문의사항",
        #         "content": "I am in my house"
        # }

@pytest.mark.asyncio
async def test_deleteNotice():
    async with AsyncClient(app = app ,base_url = baseUrl) as client:
        response = await client.delete("/api-customercenter/notice", params={"id": ObjectId(noticeId)})

        assert response.status_code == 200
        # assert response.json() == {
        #         "_id": id,
        #         "date": time,
        #         "title": "문의사항",
        #         "content": "I'm in my house"
        # }