from bs4 import BeautifulSoup
import urllib.request

url = 'https://en.wikipedia.org/wiki/LeBron_James'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'class': 'infobox vcard'})
results = table.findAll('td')
for result in results:
    print(result.text)
#for result in results:
    #print("position: " + result[1].text + "league: " + result[2].text ... etc
