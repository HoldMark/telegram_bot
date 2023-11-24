from db.database import connection

cursor = connection.cursor()


def get_expressions(get_all=False):

    select_query = 'SELECT expression FROM expressions'

    if not get_all:
        select_query += ' WHERE is_hidden = False'

    cursor.execute(select_query)
    result = cursor.fetchall()

    return result
