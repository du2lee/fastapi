from fastapi import APIRouter, Body, Depends, status
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    tags=['authentication'],
    responses={404: {"description": "not found"}, 200: {"description": "ok"}},
)

