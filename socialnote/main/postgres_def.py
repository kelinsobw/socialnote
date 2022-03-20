import psycopg2
from socialnote.settings import DATABASES

"""{'table_name': 'fsd', 'table_description': 'gfsda', 'table_privates': 'None', 'base_1': 'htgfd', 'type_1': 'Ch', 
'base_2': '', 'type_2': 'Ch', 'base_3': '', 'type_3': 'Ch', 'base_4': '', 'type_4': 'Ch', 'base_5': '', 'type_5': 'Ch', 
'base_6': '', 'type_6': 'Ch', 'base_7': '', 'type_7': 'Ch', 'base_8': '', 'type_8': 'Ch'}
"""


def create_table(info_base):
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    request_base = (f'CREATE TABLE {info_base.get("table_name")} '
               f'(ID INT PRIMARY KEY NOT NULL,')
    column = []

    for key, value in info_base.items():
        if key != "table_name" or key != "table_description":
            if str(key[0:4]) == "base" and value != "":
                column.append(value)
            if str(key[0:4]) == "type":
                column.append(value)
            if str(key[0:4]) == "base" and value == "":
                break

    for i in range(0, len(column), 2):
        request_base = " ".join([request_base, str(column[i])])
        request_base = " ".join([request_base, str(column[i + 1])])
        request_base = " ".join([request_base, ","])
    request_base = request_base[:-1]
    request_base = "".join([request_base, ");"])
    cur.execute(request_base)
    con.commit()
    con.close()

def get_the_date(table_name):
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    request_base = (f'SELECT column_name FROM {table_name}; ')
    cur.execute(request_base)
    data = cur.fetchall()
    request_base = (f'SELECT * FROM {table_name}; ')
    cur.execute(request_base)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data
