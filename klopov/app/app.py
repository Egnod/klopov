from fastapi import FastAPI
from loguru import logger

from klopov import __project__, __version__
from klopov.app.middlewares import set_middlewares
from klopov.app.routers import set_routers
from klopov.core.database.utils import (
    auto_populate_collections,
    close_db_connect,
    open_db_connect,
)


def create_app() -> FastAPI:
    logger.info("Start create app object")

    app = FastAPI(
        title=__project__,
        version=__version__,
        on_startup=[open_db_connect, auto_populate_collections],
        on_shutdown=[close_db_connect],
        docs_url=None,
        redoc_url="/api/docs",
    )

    app = set_middlewares(app)
    app = set_routers(app)

    logger.info("Complete create app object")
    return app
