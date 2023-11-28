from insight_api.PostgresConnection import PostgresConnection


# TODO: add filter for top N only.
def find_book_ratings(minimum_ratings) -> []:
    # TODO: make async somehow.
    cur = PostgresConnection().get_connection().cursor()
    query = """
    SELECT book_id, AVG(score) as avg_score FROM hafifa.ratings GROUP BY book_id HAVING COUNT(*) > %s;
    """
    data = (minimum_ratings,)

    cur.execute(query, data)

    rows = cur.fetchall()

    cur.close()

    return rows
