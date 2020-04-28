from bs4 import BeautifulSoup
import urllib.request

url = 'https://en.wikipedia.org/wiki/LeBron_James'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'class': 'infobox vcard'})
results = table.findAll('td')
for result in results[1:7]:
    print(result.text)
#Output:

#Jakes-MacBook-Air:src Jake$ python3 Scrape.py
#Small forward
#NBA
#(1984-12-30)
#American
#6 ft 9 in (2.06 m)
#250 lb (113 kg)
