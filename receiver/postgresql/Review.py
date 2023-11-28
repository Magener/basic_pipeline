from receiver.PostgresConnection import PostgresConnection


# TODO: separate afterwards
# strategy?
# when should I cur.close?
def commit_review(reviewer_id, book_id, score):
    cur = PostgresConnection().get_connection().cursor()
    query = """INSERT INTO hafifa.ratings(reviewer_id, book_id, score) VALUES (%s, %s, %s);"""  # TODO: why not use fstring?
    data = (reviewer_id, book_id, score)

    print(data)
    cur.execute(query, data)

    if cur.rowcount == 0:
        raise RuntimeError(
            f"Insertion has failed: {cur.statusmessage}")  # TODO; separate as a different exception & catch it

    print(cur.statusmessage)

    PostgresConnection().get_connection().commit()

    cur.close()

# for making queries:
"""
    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Display fetched rows
    for row in rows:
        print(row)"""
