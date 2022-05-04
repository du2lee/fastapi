from typing import Optional
from fastapi import FastAPI
from database.mongoDB import *
from routers.customerCenter import router as customerCenterRouter
from routers.auth import router as authRouter
from pathlib import Path
import logging.config, os, logging


logger = logging.getLogger(__name__)

tags_metadata = [
    {
        "name": "payment",
    },
    {
        "name": "login",
    },
]


def createApp() -> FastAPI:
    app = FastAPI()
    return app


app = createApp()

#routers
app.include_router(customerCenterRouter, prefix="/api-customercenter")
app.include_router(authRouter, prefix="/api-auth")

@app.on_event("startup")
async def onAppStart():
    await connectMongo()


@app.on_event("shutdown")
async def onAppShutdown():
    await disconnectMongo()
