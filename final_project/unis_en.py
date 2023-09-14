#Renting_extraction

from IPython.core.display import HTML
from IPython.display import IFrame
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import os

url = "https://www.studentcrowd.com/page/cheapest-uk-cities-for-student-accommodation"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content)
cities = soup.find_all('h3', class_="league-table-card-extended__header__content__title")

#The code that caused this warning is on line 14 of the file C:\Users\saski\py4e\spiced\github\playground\final_project\unis_en.py. To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

uk_cities = []
for i in cities:
    uk_cities.append(i.get_text())
uk_cities #regex to only collect numbers or slice it

city_rent = ['Carmarthen, Wales',
 'Bradford, England',
 'Bolton, England',
 'Carlisle, England',
 'Sunderland, England',
 'Preston, England',
 'Middlesbrough, England']

df = pd.DataFrame([entry.split(', ') for entry in city_rent], columns=['City', 'Country'])

# Display the DataFrame
print(df)

