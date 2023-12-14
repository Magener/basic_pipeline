from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import status

from insight_api.consts import HOST, MIN_RATINGS_FOR_INCLUSION, PORT
from insight_api.log import logger
from temporarily_shared_files.sql_alchemy.AsyncPostgresConnection import AsyncPostgresConnection


# Allows for tear down, yield separates set up from tear down parts
from temporarily_shared_files.sql_alchemy.DBEndpoint import DBEndpoint


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await AsyncPostgresConnection().close()


app = FastAPI(lifespan=lifespan)


@app.get('/api/books/')
async def get_books(presented_amount: int = None):
    try:
        books_command = DBEndpoint.get_command_parser().parse_command({"name": "find_top_rated_books", "args": {
            "minimum_ratings": MIN_RATINGS_FOR_INCLUSION,
            "presented_amount": presented_amount}
                                                                       })

        return await books_command
    except BaseException as e:
        logger.error(f"An error has occurred {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error has occurred")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
