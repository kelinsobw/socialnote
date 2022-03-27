import random

import psycopg2
from socialnote.settings import DATABASES




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
               f'(ID SERIAL,')
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
    try:
        request_base = (f'SELECT * FROM "{table_name}"; ')
        cur.execute(request_base)
        data = [cur.fetchall()]
        con.commit()
        con.close()
        data = [view_colums_table(table_name), data]
        return data
    except:
        return("Basa emply")


def view_colums_table(table_name):
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    request_base = (f"SELECT column_name FROM INFORMATION_SCHEMA.columns where table_name='{table_name}'; ")
    cur.execute(request_base)
    colums_name = cur.fetchall()
    con.commit()
    con.close()
    return colums_name


def view_column_type(table_name):
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    request_base = (f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}' ORDER BY ordinal_position; ")
    cur.execute(request_base)
    colums_type = cur.fetchall()
    con.commit()
    con.close()
    return colums_type


def add_an_enrty(table_name, data):
    print(data) #{'base_1': '1', 'base_2': '1'}
    print(table_name)
    str_request = (f"INSERT INTO {table_name} VALUES ({random.randint(2, 10000)}")
    for key in data:
        str_request = str_request + (f", '{data.get(key)}'")
    str_request = str_request + (f");")
    print(str_request)
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    cur.execute(str_request)
    con.commit()
    con.close()


def delete_record(db_name, id):
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    request_base = (
        f"DELETE FROM {db_name} WHERE ID = '{id}'; ")
    cur.execute(request_base)
    con.commit()
    con.close()
