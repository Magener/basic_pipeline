import signal
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


from insight_api.consts import MIN_RATINGS_FOR_INCLUSION, PORT, HOST
from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection
from insight_api.postgres.Review import find_book_ratings

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await AsyncPostgresConnection().close()

app = FastAPI(lifespan=lifespan)

@app.get('/api/books')
async def get_books():
    return await find_book_ratings(MIN_RATINGS_FOR_INCLUSION)


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
