import requests
from bs4 import BeautifulSoup

# senate
# page = requests.get("https://msa.maryland.gov/msa/mdmanual/05sen/html/sendist.html")

# house
# page = requests.get("https://msa.maryland.gov/msa/mdmanual/06hse/html/hsedist.html")


scraper  = BeautifulSoup(page.content, 'html.parser')
body = scraper.body

with open('urls.txt', 'a') as f:
    for link in scraper.find_all('a'):
        f.write("https://msa.maryland.gov")
        f.write(link.get('href'))
        f.write("\n")
