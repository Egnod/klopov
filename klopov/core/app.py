from fastapi import FastAPI
from loguru import logger

from klopov import __project__, __version__
from klopov.core.database.utils import close_db_connect, open_db_connect
from klopov.core.middlewares import set_middlewares
from klopov.core.routers import set_routers


def create_app() -> FastAPI:
    logger.info("Start create app object")

    app = FastAPI(
        title=__project__,
        version=__version__,
        on_startup=[open_db_connect],
        on_shutdown=[close_db_connect],
        docs_url=None,
        redoc_url="/api/docs",
    )

    app = set_middlewares(app)
    app = set_routers(app)

    logger.info("Complete create app object")
    return app
