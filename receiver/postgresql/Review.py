from receiver.PostgresConnection import PostgresConnection


# TODO: separate afterwards & complete in Review.py on insight_api as wel
# strategy?
# when should I cur.close?
from receiver.log import logger


def commit_review(reviewer_id, book_id, score):
    cur = PostgresConnection().get_connection().cursor()
    query = """INSERT INTO hafifa.ratings(reviewer_id, book_id, score) VALUES (%s, %s, %s);"""  # TODO: why not use fstring?
    data = (reviewer_id, book_id, score)

    cur.execute(query, data)
    logger.debug(f"Regstered {data} in database.")

    if cur.rowcount == 0:
        raise RuntimeError(
            f"Insertion has failed: {cur.statusmessage}")  # TODO; separate as a different exception & catch it

    PostgresConnection().get_connection().commit()

    cur.close()

