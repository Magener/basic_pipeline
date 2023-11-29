from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection


async def find_top_rated_books(minimum_ratings, presented_amount=None):
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = 'SELECT book_id, AVG(score) as avg_score FROM hafifa.ratings GROUP BY book_id HAVING COUNT(*) > $1 ORDER BY avg_score DESC $2;'
    optional_query_limitation = "LIMIT $3" if presented_amount else ""

    print(QUERY)
    result = await connection.fetch(QUERY, minimum_ratings, optional_query_limitation, presented_amount)

    result = [dict(row) for row in result]

    return result
