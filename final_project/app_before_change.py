import streamlit as st
from IPython.core.display import HTML
from IPython.display import IFrame
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import os
import logging
import pandas as pd
import numpy as np

import sqlalchemy  # use a version prior to 2.0.0 or adjust creating the engine and df.to_sql()
# from sqlalchemy import create_engine, text #this line is from chatgpt
from sqlalchemy import text
import psycopg2 as pg
import time
import logging
from study_programs import de_programs, en_areas, df, df1, de_degree
# pd.read_csv -> also read the list into it ; this way I can read tables in .csv (comma separated)

# postgres db definitions. HEADS UP: outsource these credentials and don't push to github.
USERNAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
HOST_PG = 'localhost'  # my_postgres is the hostname (= service in yml file)
PORT_PG = 5432
DATABASE_NAME_PG = 'en_de_comparison'

user_input = "maths"

conn_string_pg = f"postgresql://{USERNAME_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_NAME_PG}"
# engine = create_engine(conn_string_pg)
pg = sqlalchemy.create_engine(conn_string_pg)
# print(conn_string_pg) # controll

connection = pg.connect()

print(de_programs)
# potentially outsource the streamlit code:
st.set_page_config(layout="wide")
st.title("Come to study in Germany")
st.markdown("compare your study choice and living expanses in England and Germany")
st.header("Search your choice out of 650 english speaking Bachelor and Master programms")
st.subheader("no tuition fee in Germany - take your chances")
st.caption("Please select a study program in England or Germany")


# option = st.selectbox('Please select between master and bachelor degree:', (de_degree)) # output: study fields

unique_degree_query = "SELECT DISTINCT Degree FROM de_degree_field_title_uni_city;"
de_degrees = connection.execute(text(unique_degree_query))
degree_list = [i[0] for i in de_degrees]
option1 = st.selectbox("Please select what type of degree you are looking for:", (degree_list))

unique_field_query = f"SELECT DISTINCT Field FROM de_degree_field_title_uni_city WHERE Degree = '{option1}';"
de_fields = connection.execute(text(unique_field_query))
fields_list = [i[0] for i in de_fields]
option2 = st.selectbox("Please select the field of study you are looking for:", (fields_list))

# option3 = st.selectbox('Please select an english area:', (en_areas))

rent = st.slider('some text', 0, 800, 400)  # 0 -> min value, 130 max, 3. value: starting point
st.write("This much you are willing to pay", rent, 'euro per semester. this is the uni options')

# df / df1 are query-outputs
#st.table(df)  # df_master_bachelor
#st.dataframe(df1, use_container_width=True)

# sql_df1 = pd.read_sql(
#     f"select from de_degree_field_title_uni_city where de_fee_euro_country_change <= {fee};",
#     con=connection)   # con - is pandas name for the argument connection



# export to different file (with queries; just f-string); query_1 = query_de
query_1 = f"SELECT d.University, d.Study_program, d.City, r.Rent_monthly_pounds FROM de_degree_field_title_uni_city d INNER JOIN de_city_rent_month_rent_yr r ON d.City = r.City WHERE d.Degree = '{option1}' AND d.Field = '{option2}' AND r.Rent_monthly_pounds <= {rent};"

sql_df = pd.read_sql(query_1, con=connection)

st.dataframe(sql_df, use_container_width=True, hide_index=True)

# query_2 = f"SELECT d.\dt


# dataframe 2
#sql_df2 = pd.read_sql(query2, con=connection)

#st.dataframe(sql_df1, use_container_width=True, hide_index=True)