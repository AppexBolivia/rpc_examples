import psycopg2

# Login to Odoo server
url = 'http://localhost:8069'
db = 'v15'
username = 'test'
password = 'test'
conn = psycopg2.connect(dbname=db, user=username, password=password, host='localhost')
cur = conn.cursor()
query = """
        SELECT
            move.name AS move_name,
            move.date AS move_date,
            move.ref AS move_ref,
            move.journal_id AS journal_id,
            array_agg(line.id) AS line_ids
        FROM
            account_move move
        INNER JOIN
            account_move_line line ON line.move_id = move.id
        GROUP BY
            move.id
    """

# Execute the query
cur.execute(query)
# Fetch the results
move_ids = cur.fetchall()
# 'name', 'date', 'ref', 'journal_id', 'line_ids'
for move in move_ids:
    print({
        'name': move[0],
        'date': move[1].strftime('%Y-%m-%d'),
        'ref': move[2] or False,
        'journal_id': move[3],
        'line_ids': move[4]
    })
