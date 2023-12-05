from typing import List, Dict

from insight_api.postgres.AsyncPostgresConnection import AsyncPostgresConnection


async def find_top_rated_books(minimum_ratings: int, presented_amount: int = None) -> List[Dict]:
    async with await AsyncPostgresConnection.get_connection() as connection:
        optional_query_limitation = "LIMIT $2" if presented_amount else ""
        optional_query_argument = [presented_amount] if presented_amount else []

        QUERY = 'SELECT book_id, AVG(score) as avg_score FROM hafifa.ratings ' \
                'GROUP BY book_id HAVING COUNT(*) > $1 ' \
                f'ORDER BY avg_score DESC {optional_query_limitation}'

        result = await connection.fetch(QUERY, minimum_ratings, *optional_query_argument)

        return [dict(row) for row in result]
