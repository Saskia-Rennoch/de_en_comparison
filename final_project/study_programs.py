import pandas as pd
import numpy as np

de_programs = ["maths", "biology", "food_science"]

de_fields = ["IT", "Medicine"]

Fields = "something"

de_degree = ["Master", "Bachelor"]

en_unis = ["university_list"]

en_areas = ["areas"]

#query_1 = f"""ae , ue oe"""

#sql_df1 = pd.read_sql(query_1, con=connection)

# Replace "ae" with "ä", "oe" with "ö", and "ue" with "ü" in the dataframe
# exchange = query_1.replace({"ae": "ä", "oe": "ö", "ue": "ü"}, regex=True)
# print(exchange)
# make connection to postgres
# df = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=('col %d' % i for i in range(5)))
query_1 = "This is an example with ae, oe, and ue."

# Replace "ae" with "ä", "oe" with "ö", and "ue" with "ü" in the string
exchange = query_1.replace("ae", "ä").replace("oe", "ö").replace("ue", "ü")
print(exchange)

query_3 = f"""SELECT p.study_oeprogramme, p.uniueversity, e.raeent_monthly_pounds, e.rent_year_pounds, e.approx_tuition_fee_yr
        FROM en_reg_uni_rent_m_yr_fee e
        INNER JOIN en_programmes p ON e.university = p.university
    WHERE e.region = '{option3}' AND e.university = '{option4}' AND e.rent_monthly_pounds <= {rent_en};"""


sql_df3 = pd.read_sql(query_3, con=connection)

sql_df3 =sql_df3.replace({"ae": "ä", "oe": "ö", "ue": "ü"}, regex=True)

st.dataframe(sql_df3, use_container_width=True, hide_index=True)