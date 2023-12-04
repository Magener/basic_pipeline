from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection


async def find_top_rated_books(minimum_ratings, presented_amount=None):
    connection = await AsyncPostgresConnection().get_connection()

    optional_query_limitation = "LIMIT $2" if presented_amount else ""
    optional_query_argument = [presented_amount] if presented_amount else []

    BOOK_SCORE_QUERY = 'SELECT book_id, AVG(score) as avg_score FROM hafifa.ratings ' \
                       'GROUP BY book_id HAVING COUNT(*) > $1 ' \
                       f'ORDER BY avg_score DESC {optional_query_limitation}'

    BOOK_NAME_AND_SCORES_QUERY = f"SELECT score.book_id, book.book_name, score.avg_score FROM ({BOOK_SCORE_QUERY}) score " \
                                 "LEFT JOIN hafifa.book book ON score.book_id=book.book_id"

    result = await connection.fetch(BOOK_NAME_AND_SCORES_QUERY, minimum_ratings, *optional_query_argument)

    result = [dict(row) for row in result]

    return result
