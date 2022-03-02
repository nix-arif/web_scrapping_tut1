from email import header
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://www.hubertiming.com/results/2018MLK'
html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")
title = soup.title
print(title.text)

links = soup.find_all('a', href=True)

# for link in links:
#   print(link['href'])

data = []

allrows = soup.find_all('tr')
for row in allrows:
  row_list = row.find_all('td')
  dataRow = []
  for cell in row_list:
    dataRow.append(cell.text.strip())
  data.append(dataRow)

# print(data[5:10])
data = data[5:]

df = pd.DataFrame(data)


header_list = []
col_headers = soup.find_all('th')

for col in col_headers:
  header_list.append(col.text)

df.columns = header_list
# print(df.head())
# print(df.info())
# print(df.shape)

df2 = df.dropna(axis=0, how='any')


df2['ChipTime_minutes'] = pd.to_timedelta(df2['Chip Time'])

