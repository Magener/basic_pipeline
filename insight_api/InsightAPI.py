import signal
from contextlib import asynccontextmanager

import uvicorn
from asyncpg import PostgresError
from fastapi import FastAPI, HTTPException

from insight_api.consts import MIN_RATINGS_FOR_INCLUSION, PORT, HOST
from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from insight_api.postgres.Review import find_top_rated_books


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
        print(f"An error has occurred {e}") #TODO; set as a logger.
        raise HTTPException(status_code=500, detail="An error has occurred")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
