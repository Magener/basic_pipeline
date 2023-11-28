from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection


# TODO: ensure exception handling.
async def find_book_ratings(minimum_ratings):
    connection = await AsyncPostgresConnection().get_connection()

    QUERY = 'SELECT book_id, AVG(score) as avg_score FROM hafifa.ratings GROUP BY book_id HAVING COUNT(*) > $1 ORDER BY avg_score DESC;'
    result = await connection.fetch(QUERY, minimum_ratings)

    result = [dict(row) for row in result]

    return result
