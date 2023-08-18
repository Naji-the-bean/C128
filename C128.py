from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests as req

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"


#browser = webdriver.Chrome("chromedriver.exe")
page = req.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
star_table=soup.find_all("table",{"class:wikitable sortable"})
total_table = len(star_table)
temp_list=[]
table_rows = star_table[1].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_names=[]
distance=[]
mass=[]
radius=[]
print(temp_list)
for a in range(1,len(temp_list)):
    star_names.append(temp_list[a][0])
    distance.append(temp_list[a][5])
    mass.append(temp_list[a][7])
    radius.append(temp_list[a][8])
headers = ["star_name","distance","mass","radius"]
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=headers)
print(df)
df.to_csv("dwarfs.csv",index=True,index_label="id")