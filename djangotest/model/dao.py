from django.db import connection

__author__ = 'jonathan'


# executes the statement and makes a pretty dict for rendering
def convert_to_dict(cursor):
    columns = [col[0] for col in cursor.description]
    rows = [tuple(row) for row in cursor.fetchall()]
    print(rows)
    result = {'columns': columns, 'rows': rows}
    return result


def select_all(table_name):
    query_string = "SELECT * FROM " + table_name
    cursor = connection.cursor()
    cursor.execute(query_string)
    return convert_to_dict(cursor)
