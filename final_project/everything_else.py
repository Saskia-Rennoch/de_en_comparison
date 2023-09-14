import streamlit as st
from IPython.core.display import HTML
from IPython.display import IFrame
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import os
import logging

import sqlalchemy  # use a version prior to 2.0.0 or adjust creating the engine and df.to_sql()
# from sqlalchemy import create_engine, text #this line is from chatgpt
import psycopg2 as pg
import time
import logging
from app import option, option2, option3

# postgres db definitions. HEADS UP: outsource these credentials and don't push to github.
USERNAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
HOST_PG = 'localhost'  # my_postgres is the hostname (= service in yml file)
PORT_PG = 5432
DATABASE_NAME_PG = 'en_de_comparison'    # 'reddits_pgdb'


user_input = "maths"

conn_string_pg = f"postgresql://{USERNAME_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_NAME_PG}"
#engine = create_engine(conn_string_pg)
pg = sqlalchemy.create_engine(conn_string_pg)
print(conn_string_pg) #controll

connection = pg.connect()
#logging.critical("")

if user_input == option:
    continue
else:
    dfjsdf



#query with this connection
query_user_input = """SELECT city, rent FROM TABLE1 WHERE subject = {user_input};"""
# create_table_string = """CREATE TABLE IF NOT EXISTS comparison(
#     time TEXT,
#     comparison TEXT,
#     sentiment NUMERIC);"""
#create the table in postgres

query_user_input2 = "blub"  # input: en_city output: en_uni; en

query_user_input3 = "blub2"

if user_input == option:
    query_completer = query_user_input # reihenfolge muss geändert werden
elif user_input == option2:
    query_completer = query_user_input2

elif user_input == option3:
    query_completer = query_user_input3

try:
    connection.execute(sqlalchemy.text(query_completer))
    connection.commit()
    logging.critical("\n---- successfully created table in postgres ----\n")
except:
    logging.exception("\n---- could not create table in postgres ----\n")


run = False
if run:
    time.sleep(7)  # safety margine to ensure running postgres server
    #open the connection
    pg = sqlalchemy.create_engine(conn_string_pg)#.connect() #neu -> connect()

    conn = pg.connect()#neu



    #pg.execute(sqlalchemy.text(create_table_string))
    #pg.commit() #neu
    #conn.close()
    # create_table_string = sqlalchemy.text("""CREATE TABLE IF NOT EXISTS reddits (
    #                                          time TEXT,
    #                                          reddit TEXT,
    #                                          sentiment NUMERIC
    #                                          );

    #                                       """)
    # pg.execute(create_table_string)
