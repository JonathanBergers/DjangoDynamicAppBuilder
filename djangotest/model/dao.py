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
    import pymssql
    conn = pymssql.connect(server='192.168.0.114', user='admin', password='admin',
    database='jonathan', as_dict=True)
    cursor = conn.cursor()
    cursor.execute("SELECT *  FROM " + table_name)
    # print(conn)

    return cursor.fetchall()




def get_information_scheme(table_name):
    import _mssql
    conn = _mssql.connect(server='192.168.0.114', user='admin', password='admin',
    database='jonathan')
    conn.execute_query('SELECT * FROM INFORMATION_SCHEMA.TA')

    for row in conn:
        print(row)