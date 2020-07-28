from fastapi import APIRouter, FastAPI
from loguru import logger


def set_routers(app: FastAPI) -> FastAPI:
    logger.info("Start collecting routers")

    api_router = APIRouter()

    # api_router.include_router(account.router, prefix="/account", tags=["account"])

    app.include_router(api_router, prefix="/api")

    logger.info("Complete collecting routers")

    return app
