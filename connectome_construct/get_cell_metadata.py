from urllib import request
from bs4 import BeautifulSoup
import re

data_url = 'http://www.wormatlas.org/celllistsulston.htm'

url = request.urlopen(data_url).read()
soup = BeautifulSoup(url)

table = soup.find_all('table')[4]

all_data = []
for row in table.find_all('tr')[1:]:
    data = []
    for cell in row.find_all('p'):
        data.append(cell.string)

    all_data.append(data)

new_data = []

for row in all_data:
    if not row:
        continue

    if 'L/R' in row[0]:
        original = row[0]
        row[0] = original.replace('L/R', 'L')
        new_data.append(row.copy())
        row[0] = original.replace('L/R', 'R')
        new_data.append(row.copy())
    else:
        new_data.append(row.copy())


all_data2 = ['|'.join(row) for row in new_data]

all_data3 = []
for row in all_data2:
    all_data3.append(re.sub('\s{2,}', ' ', row))

out = '\n'.join(all_data3)

with open('test.psv', 'w') as out_file:
    out_file.write(out)