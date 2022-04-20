import os, pytest, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from httpx import AsyncClient
from bson.objectid import ObjectId
from fastapi.testclient import TestClient
from app import app



# client = TestClient(app)
# def test_getFaqs():
#     response = client.get("/faqs")

#     assert response.json() == {}
#     assert response.status_code == 200








baseUrl = "http://127.0.0.1:9001"

@pytest.mark.asyncio
async def test_postFaq():
    global id, time
    async with AsyncClient(base_url = baseUrl) as client:
        response = await client.post("/api-customercenter/faq", 
        json={
                "category" : "중요!!",
                "title" : "문의사항",
                "content" : "I wanna go home",
            })
        id = response.json()['_id']
        time = response.json()['CreatedAt']

        assert response.status_code == 201

@pytest.mark.asyncio
async def test_getFaq():
    async with AsyncClient(base_url = baseUrl) as client:
        response = await client.get("/api-customercenter/faq", params={"id": ObjectId(id)})

        assert response.status_code == 200
        assert response.json() == {
                "_id": id,
                "CreatedAt": time,
                "Category": "중요!!",
                "Title": "문의사항",
                "Content": "I wanna go home"
        }

@pytest.mark.asyncio
async def test_getFaqs():
    async with AsyncClient(base_url = baseUrl) as client:
        response = await client.get("/api-customercenter/faqs")

        assert response.status_code == 200

@pytest.mark.asyncio
async def test_updateFaq():
    global id, time
    async with AsyncClient(base_url = baseUrl) as client:
        response = await client.patch("/api-customercenter/faq", params={"id": ObjectId(id)},
        json={
                "category" : "잡담",
            })
        id = response.json()['_id']
        time = response.json()['CreatedAt']

        assert response.status_code == 200
        assert response.json() == {
                "_id": id,
                "CreatedAt": time,
                "Category": "잡담",
                "Title": "문의사항",
                "Content": "I wanna go home"
        }

@pytest.mark.asyncio
async def test_deleteFaq():
    async with AsyncClient(base_url = baseUrl) as client:
        response = await client.delete("/api-customercenter/faq", params={"id": ObjectId(id)})

        assert response.status_code == 200
        assert response.json() == {
                "_id": id,
                "CreatedAt": time,
                "Category": "잡담",
                "Title": "문의사항",
                "Content": "I wanna go home"
        }