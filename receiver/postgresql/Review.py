from receiver.PostgresConnection import PostgresConnection


# TODO: separate afterwards & complete in Review.py (after converting to async)
from receiver.log import logger


def commit_review(reviewer_id, book_id, score):
    cur = PostgresConnection().get_connection().cursor()
    query = """INSERT INTO hafifa.ratings(reviewer_id, book_id, score) VALUES (%s, %s, %s);"""
    data = (reviewer_id, book_id, score)

    cur.execute(query, data)
    logger.debug(f"Regstered {data} in database.")

    if cur.rowcount == 0:
        raise RuntimeError(
            f"Insertion has failed: {cur.statusmessage}")

    PostgresConnection().get_connection().commit()

    cur.close()

