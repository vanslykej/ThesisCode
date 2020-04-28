from bs4 import BeautifulSoup as bs
import urllib.request as url
import wikipedia as w
import re

d = {}

w.set_lang('en')
s = w.page(w.search('List of current NBA team rosters')[0])
html = url.urlopen(s.url).read()
soup = bs(html, 'html.parser')

table1 = soup.findAll('table')[1]
for row in table1.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table2 = soup.findAll('table')[3]
for row in table2.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table3 = soup.findAll('table')[5]
for row in table3.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table4 = soup.findAll('table')[7]
for row in table4.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table5 = soup.findAll('table')[9]
for row in table5.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table6 = soup.findAll('table')[11]
for row in table6.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table7 = soup.findAll('table')[13]
for row in table7.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table8 = soup.findAll('table')[15]
for row in table8.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table9 = soup.findAll('table')[17]
for row in table9.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table10 = soup.findAll('table')[19]
for row in table10.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table11 = soup.findAll('table')[21]
for row in table11.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table12 = soup.findAll('table')[23]
for row in table12.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table13 = soup.findAll('table')[25]
for row in table13.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table14 = soup.findAll('table')[27]
for row in table14.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table15 = soup.findAll('table')[29]
for row in table15.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table16 = soup.findAll('table')[31]
for row in table16.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table17 = soup.findAll('table')[33]
for row in table17.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table18 = soup.findAll('table')[35]
for row in table18.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table19 = soup.findAll('table')[37]
for row in table19.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table20 = soup.findAll('table')[39]
for row in table20.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table21 = soup.findAll('table')[41]
for row in table21.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table22 = soup.findAll('table')[43]
for row in table22.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table23 = soup.findAll('table')[45]
for row in table23.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table24 = soup.findAll('table')[47]
for row in table24.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table25 = soup.findAll('table')[49]
for row in table25.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table26 = soup.findAll('table')[51]
for row in table26.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table27 = soup.findAll('table')[53]
for row in table27.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table28 = soup.findAll('table')[55]
for row in table28.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table29 = soup.findAll('table')[57]
for row in table29.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

table30 = soup.findAll('table')[59]
for row in table30.findAll('tr'):
    for colnum, col in enumerate(row.find_all('td')):
        if (colnum+1) % 6 == 3:
            a = col.find('a')
            link = 'https://en.wikipedia.org' + a.get('href')
            d[a.get('title')] = {}
            d[a.get('title')]['link'] = link

for players, data in d.items():
    page = bs(url.urlopen(data['link']).read(), 'html.parser')

lst = []
for key, val in d.items():
    if val is not None:
        for _,sub_val in val.items():
            lst.append(sub_val)
            for idx, player_lnk in enumerate(lst):
                print(lst)

import urllib.request

for idx, url in enumerate(lst):
    page = urllib.request.urlopen(url)
    player_soup = bs(page, 'html.parser')
    table = player_soup.find('table', attrs={'class': 'infobox vcard'})
    results = table.findAll('td')
    for result in results[1:7]:
        print(result.text)



#print((soup.find(text = "Position").findNext('td').contents[0]).text)
#print((soup.find(text = "League").findNext('td').contents[0]).text)
#print((soup.find(text = "Born").findNext('td').contents[0]).text)
#print((soup.find(text = "Nationality").findNext('td').contents[0]))
#print((soup.find(text = "Listed height").findNext('td').contents[0]))
#print((soup.find(text = "Listed weight").findNext('td').contents[0]))

#Output:

#Jakes-MacBook-Air:src Jake$ python3 Take1.py
#Traceback (most recent call last):
#  File "Take1.py", line 34, in <module>
#    print((soup.find(text = "Position").findNext('td').contents[0]).text)
#AttributeError: 'NoneType' object has no attribute 'findNext'
