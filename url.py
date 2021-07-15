import requests
from bs4 import BeautifulSoup

# md senate
# page = requests.get("https://msa.maryland.gov/msa/mdmanual/05sen/html/sendist.html")

# md house
# page = requests.get("https://msa.maryland.gov/msa/mdmanual/06hse/html/hsedist.html")

# va senate
page = requests.get("https://apps.senate.virginia.gov/Senator/index.php")


scraper  = BeautifulSoup(page.content, 'html.parser')
body = scraper.body

with open('urls.txt', 'a') as f:
    for link in scraper.find_all('a'):
        f.write("https:")
        f.write(link.get('href'))
        f.write("\n")
