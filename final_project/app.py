import streamlit as st
#from IPython.core.display import HTML
#from IPython.display import IFrame
import requests
import pandas as pd
import re
#from bs4 import BeautifulSoup
import os
import logging
import pandas as pd
import numpy as np

import sqlalchemy  # use a version prior to 2.0.0 or adjust creating the engine and df.to_sql()
from sqlalchemy import text
import psycopg2 as pg
# import time
import logging

USERNAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
HOST_PG = 'localhost'
PORT_PG = 5432
DATABASE_NAME_PG = 'en_de_comparison'

conn_string_pg = f"postgresql://{USERNAME_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_NAME_PG}"
pg = sqlalchemy.create_engine(conn_string_pg)

connection = pg.connect()



# print(de_programs)
st.set_page_config(layout="wide")
st.title("Come to study in Germany")

nav = st.sidebar.radio(
    "Please chose one of the following options:",
    ["Home", "Germany", "England"])

# nav == "Home"

if nav == "Home":
    st.markdown("compare your study choice and living expanses in England and Germany")
    st.header("Search your choice out of 650 English speaking Bachelor and Master programms")
    st.subheader("no tuition fee in Germany - take your chances")
    st.caption("Please choose between the selections England or Germany on the left side")

    col1, col2 = st.columns(2)

# Add the first image to the first column
    col1.image("https://www.england.de/images/england/england-flaggen.jpg")
    col1.text("Source: https://www.england.de/")

    # Add the second image to the second column
    col2.image("https://media.istockphoto.com/id/619638736/de/foto/altstadt-von-rothenburg-ob-der-tauber-franken-bayern-deutschland.jpg?s=1024x1024&w=is&k=20&c=oFTlJ7ePTMULw3XZy75DNDPAQB8umJZV8jh5-pIEDKo=")
    col2.text("Source: https://www.istockphoto.com/")


elif nav == "Germany":
    unique_degree_query = "SELECT DISTINCT Degree FROM de_degree_field_title_uni_city;"
    de_degrees = connection.execute(text(unique_degree_query))
    degree_list = [i[0] for i in de_degrees]
    option1 = st.selectbox("Please select what type of degree you are looking for:", (degree_list))

    unique_field_query = f"SELECT DISTINCT Field FROM de_degree_field_title_uni_city WHERE Degree = '{option1}';"
    de_fields = connection.execute(text(unique_field_query))
    fields_list = [i[0] for i in de_fields]
    option2 = st.selectbox("Please select the field of study you are looking for:", (fields_list))

    rent = st.slider('How much rent are you willing to pay?', 0, 800, 400, key="german_rent")
    st.write("How much rent are you willing to pay", rent, 'euro per semester. this is the uni options')

    # export to different file; query_1 = query_de
    query_1 = f"""SELECT d.University, d.Study_program, d.City, r.Rent_monthly_pounds FROM de_degree_field_title_uni_city d
            INNER JOIN de_city_rent_month_rent_yr r ON d.City = r.City WHERE d.Degree = '{option1}' AND d.Field = '{option2}' AND r.Rent_monthly_pounds <= {rent};"""

    sql_df1 = pd.read_sql(query_1, con=connection)

    sql_df1 = sql_df1.replace({"ae": "ä", "oe": "ö", "ue": "ü"}, regex=True)  # chatgpt suggested change

    st.dataframe(sql_df1, use_container_width=True, hide_index=True)


    # small query (England)
    query_2 = f"""SELECT e.region,
                ROUND(AVG(e.rent_monthly_pounds)) AS avg_rent_monthly_pounds,
                ROUND(AVG(e.rent_year_pounds)) AS avg_rent_year_pounds,
                ROUND(AVG(e.approx_tuition_fee_yr)) AS avg_approx_tuition_fee_yr
            FROM en_reg_uni_rent_m_yr_fee e
            GROUP BY e.region;"""

    sql_df2 = pd.read_sql(query_2, con=connection)

    st.dataframe(sql_df2, use_container_width=True, hide_index=True)

elif nav == "England":
    # English Webpage:
    # selectionbox option3 and option4 should only appear when on the top selection between England / Germany -> En
    # selectbox 1 : select a region in england
    en_unique_region_query = "SELECT DISTINCT region FROM en_reg_uni_rent_m_yr_fee e;"
    en_regions = connection.execute(text(en_unique_region_query))
    region_list = [i[0] for i in en_regions]
    option3 = st.selectbox("Please select in which region of England you would like to study:", (region_list))

    en_unique_university_query = f"SELECT DISTINCT university FROM en_reg_uni_rent_m_yr_fee e WHERE region = '{option3}';"
    en_unis = connection.execute(text(en_unique_university_query))
    unis_list = [i[0] for i in en_unis]
    option4 = st.selectbox("Please select the university you are looking to study in:", (unis_list))

    rent_en = st.slider('How much rent are you willing to pay?', 0, 900, 400, key = "england_rent")
    st.write("This much you are willing to pay", rent_en, 'pounds per semester. this is the uni options')  # think about

    # Big query England
    query_3 = f"""SELECT p.study_programme, p.university, e.rent_monthly_pounds, e.rent_year_pounds, e.approx_tuition_fee_yr
            FROM en_reg_uni_rent_m_yr_fee e
            INNER JOIN en_programmes p ON e.university = p.university
        WHERE e.region = '{option3}' AND e.university = '{option4}' AND e.rent_monthly_pounds <= {rent_en};"""

    sql_df3 = pd.read_sql(query_3, con=connection)

    st.dataframe(sql_df3, use_container_width=True, hide_index=True)

    # Small query England (German values)
    query_4 = f"""SELECT f.County,
                ROUND(AVG(f.Tuition_fee)) AS avg_tuition_fee,
                ROUND(AVG(r.Rent_monthly_pounds)) AS avg_rent_monthly_pounds,
                ROUND(AVG(r.Rent_yearly_pounds)) AS avg_rent_yearly_pounds
                FROM de_uni_county_fee f
                JOIN de_degree_field_title_uni_city d ON f.University = d.University
                JOIN de_city_rent_month_rent_yr r ON d.City = r.City
                GROUP BY f.County;"""

    sql_df4 = pd.read_sql(query_4, con=connection)

    sql_df4 = sql_df4.replace({"ae": "ä", "oe": "ö", "ue": "ü"}, regex=True)

    st.dataframe(sql_df4, use_container_width=True, hide_index=True)
