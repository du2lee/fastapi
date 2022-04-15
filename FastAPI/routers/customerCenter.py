from fastapi import APIRouter, Body, Depends, status
from fastapi.encoders import jsonable_encoder
from services.customerCenter import FaqService
from models.customerCenter import *
from dtos.customerCenterDto import *

router = APIRouter(
    tags=['customerCenter'],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}},
)

faqService = FaqService()

# faq 생성
@router.post("/faq", description = '''**faq 생성**''',
                status_code=status.HTTP_201_CREATED)
async def addFaq(faq: Faq = Body(...)):
    faq = jsonable_encoder(faq)
    resultFaq = await faqService.addFaq(faq)
    return FaqDto(**resultFaq)

# faq 검색
@router.get("/faq", description = '''**faq 검색**''',
                status_code=status.HTTP_200_OK)
async def searchFaq(id):
    resultFaq = await faqService.searchFaq(id)
    return FaqDto(**resultFaq)

# faq 전체검색
@router.get("/faqs", description = '''**faq 전체 검색**''',
                status_code=status.HTTP_200_OK)
async def searchFaqs():
    searchFaqs = await faqService.searchFaqs()
    print('result',searchFaqs)
    array = []
    for idx in searchFaqs:
        array.append(FaqDto(**idx))
    return array

# faq 수정
@router.patch("/faq", description = '''**faq 수정**''',
                status_code=status.HTTP_200_OK)
async def updateFaq(id, faq: UpdateFaq = Body(...)):
    faq = jsonable_encoder(faq)
    resultFaq = await faqService.updateFaq(id, faq)
    return FaqDto(**resultFaq)

# faq 삭제
@router.delete("/faq", description = '''**faq 삭제**''',
                status_code=status.HTTP_200_OK)
async def deleteFaq(id):
    resultFaq = await faqService.deleteFaq(id)
    return FaqDto(**resultFaq)
