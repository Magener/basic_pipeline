import uvicorn
from fastapi import FastAPI

from insight_api.postgres.Review import find_book_ratings
from insight_api.consts import MIN_RATINGS_FOR_INCLUSION, PORT, HOST

app = FastAPI()

@app.get('/api/books')
async def get_books():
    return find_book_ratings(MIN_RATINGS_FOR_INCLUSION)


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)