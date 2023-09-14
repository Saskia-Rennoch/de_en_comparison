from IPython.core.display import HTML
from IPython.display import IFrame
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import os

uni_eng = []
for i in range (1,673): # range stops one before end
    url5 = f"https://studyqa.com/search?ord_name=&ord_price=&ord_deadline=&ord_duration=&string=&discipline=0&language=0&region-radio=country&region=5&country%5B%5D=826&city=0&tuition_min=0&tuition_max=100000&timetable=0&duration_min=1&duration_max=72&page={i}"
    response = requests.get(url5)
    html_content = response.text
    soup = BeautifulSoup(html_content)
    uni_soup = soup.find_all('h3')
    uni_eng.append(uni_soup)

# print(uni_eng)

merged_engprog = [str(item) for sublist in uni_eng for item in sublist]
merged_engprog

texts = []
for item in merged_engprog:
    soup = BeautifulSoup(item, 'html.parser')
    texts.append(soup.text)
course_inds = range(0, len(texts), 2)
university_inds = range(1, len(texts), 2)
unis = []
courses = []
for course_ind, university_ind in zip(course_inds, university_inds):
    courses.append(texts[course_ind])
    unis.append(texts[university_ind])
df = pd.DataFrame({"course": courses, "university": unis})
print(df)

df.to_csv("/data/eng_prog.csv", sep=";")