from db.database import connection

cursor = connection.cursor()


def get_expressions(get_all=False):
    select_query = """
        select
            case
                when definiton is not null and example is not null then "expression" || ' - ' || definiton || ' - ' || example
                when definiton is not null and example is null then "expression" || ' - ' || definiton
                when definiton is null and example is not null then "expression" || ' - ' || example
                when definiton is null and example is null then "expression"
            end as ex_def   from expressions e 
    """

    if not get_all:
        select_query += ' WHERE is_hidden = False'

    cursor.execute(select_query)
    result = cursor.fetchall()

    return result
