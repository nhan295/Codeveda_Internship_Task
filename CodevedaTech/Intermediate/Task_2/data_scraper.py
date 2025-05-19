import requests
import csv
from bs4 import BeautifulSoup

# send Get request to CoinGecko

url = 'https://quotes.toscrape.com/'
headers = { 'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

# select all items in coin table

rows = soup.select('.quote')

# create data list

data = []
for row in rows[:20]:
    try:
        # get name
        text = row.select_one('.text').text.strip()

        # get price
        author = row.select_one('.author').text.strip()

        data.append([text,author])

    except Exception as e:
        continue

# save to csv file
with open('quotes.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Quote','Author'])
    writer.writerows(data)
