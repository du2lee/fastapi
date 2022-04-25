from fastapi import APIRouter, Body, Depends, status
from fastapi.encoders import jsonable_encoder
from services.customerCenter import *
from models.customerCenter import *
from dtos.customerCenterDto import *

router = APIRouter(
    tags=['customerCenter'],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}},
)

faqService = FaqService()
noticeService = NoticeService()

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

# ====================================================================

# Notice 생성
@router.post("/notice", description = '''**Notice 생성**''',
                status_code=status.HTTP_201_CREATED)
async def addNotice(notice: Notice = Body(...)):
    notice = jsonable_encoder(notice)
    resultNotice = await noticeService.addNotice(notice)
    return NoticeDto(**resultNotice)

# Notice 검색
@router.get("/notice", description = '''**Notice 검색**''',
                status_code=status.HTTP_200_OK)
async def searchNotice(id):
    resultNotice = await noticeService.searchNotice(id)
    return NoticeDto(**resultNotice)

# Notice 전체검색
@router.get("/notices", description = '''**Notice 전체 검색**''',
                status_code=status.HTTP_200_OK)
async def searchNotices():
    searchNotices = await noticeService.searchNotices()
    array = []
    for idx in searchNotices:
        array.append(NoticeDto(**idx))
    return array

# Notice 수정
@router.patch("/notice", description = '''**Notice 수정**''',
                status_code=status.HTTP_200_OK)
async def updateNotice(id, notice: UpdateNotice = Body(...)):
    notice = jsonable_encoder(notice)
    resultNotice = await noticeService.updateNotice(id, notice)
    return NoticeDto(**resultNotice)

# Notice 삭제
@router.delete("/notice", description = '''**Notice 삭제**''',
                status_code=status.HTTP_200_OK)
async def deleteNotice(id):
    resultNotice = await noticeService.deleteNotice(id)
    return NoticeDto(**resultNotice)

