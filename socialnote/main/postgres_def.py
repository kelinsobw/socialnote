import psycopg2
from socialnote.settings import DATABASES

"""{'table_name': 'fsd', 'table_description': 'gfsda', 'table_privates': 'None', 'base_1': 'htgfd', 'type_1': 'Ch', 
'base_2': '', 'type_2': 'Ch', 'base_3': '', 'type_3': 'Ch', 'base_4': '', 'type_4': 'Ch', 'base_5': '', 'type_5': 'Ch', 
'base_6': '', 'type_6': 'Ch', 'base_7': '', 'type_7': 'Ch', 'base_8': '', 'type_8': 'Ch'}
"""

abbreviations = {

}


def create_table(info_base):
    con = psycopg2.connect(
        database=(DATABASES.get('default')).get("NAME"),
        user=(DATABASES.get('default')).get("USER"),
        password=(DATABASES.get('default')).get("PASSWORD"),
        host=(DATABASES.get('default')).get("HOST"),
        port=(DATABASES.get('default')).get("PORT")
    )
    cur = con.cursor()
    inquiry = (f'CREATE TABLE {info_base.get("table_name")} '
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
        inquiry = " ".join([inquiry, str(column[i])])
        inquiry = " ".join([inquiry, str(column[i + 1])])
        inquiry = " ".join([inquiry, ","])
    inquiry = inquiry[:-1]
    inquiry = "".join([inquiry, ");"])
    cur.execute(inquiry)
    con.commit()
    con.close()
