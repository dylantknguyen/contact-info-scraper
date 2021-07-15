import requests
# from bs4 import BeautifulSoup
import re

page = requests.get("https://msa.maryland.gov/msa/mdmanual/05sen/html/msa12217.html").text

phone_numbers = list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", page))
emails = list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", page))

print(phone_numbers[0])
print(emails[0])
