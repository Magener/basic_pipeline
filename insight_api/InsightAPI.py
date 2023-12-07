from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import status

from insight_api.consts import MIN_RATINGS_FOR_INCLUSION, PORT, HOST
from insight_api.log import logger
from temporarily_shared_files.sql_alchemy.AsyncPostgresConnection import AsyncPostgresConnection
from temporarily_shared_files.sql_alchemy.repositories.Review import find_top_rated_books

# Allows for tear down, yield separates set up from tear down parts
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await AsyncPostgresConnection().close()


app = FastAPI(lifespan=lifespan)


@app.get('/api/books/')
async def get_books(presented_amount: int = None):
    try:
        return await find_top_rated_books(MIN_RATINGS_FOR_INCLUSION, presented_amount)
    except BaseException as e:
        logger.error(f"An error has occurred {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error has occurred")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
