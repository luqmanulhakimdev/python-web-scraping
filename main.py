import requests
import csv
import re
from bs4 import BeautifulSoup

response = requests.get('https://onepiece.fandom.com/wiki/List_of_Canon_Characters')
soup = BeautifulSoup(response.text, 'html.parser')

with open('response.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter = ";")
    writer.writerow(['No', 'Name', 'Chapter', 'Episode', 'Year', 'Note'])
    table = soup.find_all('table')
    for index, item in enumerate(table[0].find_all('tr')):
        subitem = item.find_all('td')
        note = ''
        if subitem:
            if len(subitem) > 5:
                note = subitem[5].text.strip()
            writer.writerow([index, subitem[1].text.strip(), subitem[2].text.strip(), subitem[3].text.strip(), subitem[4].text.strip(), note])
            