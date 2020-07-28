from loguru import logger

from klopov.core.database.client import mongo_client


async def open_db_connect():
    logger.info("Starting prepopulate db")
    is_failed = None

    try:
        await mongo_client.admin.command("ping")
    except Exception as e:
        is_failed = True
        logger.error(f"Unable to connect DB, error {e.__class__.__name__}")

    if not is_failed:
        logger.info("Successfully open db connect")

    else:
        exit(-1)


async def close_db_connect():
    logger.info("Close DB connect")
