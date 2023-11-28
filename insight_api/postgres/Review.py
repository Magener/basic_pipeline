from insight_api.postgres.PostgresConnection import PostgresConnection
from insight_api.postgres.Utils import parse_to_dict


# TODO: add filter for top N only.
def find_book_ratings(minimum_ratings) -> []:
    # TODO: make async somehow.
    # TODO: convert average to number
    cur = PostgresConnection().get_connection().cursor()
    query = """
    SELECT book_id, AVG(score) as avg_score FROM hafifa.ratings GROUP BY book_id HAVING COUNT(*) > %s;
    """
    data = (minimum_ratings,)

    cur.execute(query, data)
    rows = cur.fetchall()

    result = parse_to_dict(rows, cur.description)

    cur.close()

    return result


