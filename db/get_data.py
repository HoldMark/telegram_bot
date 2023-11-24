from db.database import connection

cursor = connection.cursor()


def get_expressions():

    select_query = 'SELECT expression FROM expressions'
    cursor.execute(select_query)
    result = cursor.fetchall()

    return result
