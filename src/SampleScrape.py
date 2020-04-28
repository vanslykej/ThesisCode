from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://en.wikipedia.org/wiki/LeBron_James'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs table
stats = page_soup.findAll("table",{"class":"infobox vcard"})

filename = "lebron.csv"
f = open(filename, "w")

headers = "position"

f.write(headers)

for table in stats:
    position = table.div.div.td["role"]

    role_table = table.findAll("td", {"class":"position"})
    player_position = role_table[0].text

    print("position: " + player_position)

    f.write(position + "")

f.close()
