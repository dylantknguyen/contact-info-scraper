import requests
# from bs4 import BeautifulSoup
import re

with open('urls.txt') as f:
    for line in f:
        page = requests.get(line.strip('\n')).text

        phone_numbers = list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", page))
        emails = list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", page))

        with open('contacts.txt', 'a') as f:
            f.write(phone_numbers[0])
            f.write('\n')
            f.write(emails[0])
            f.write('\n')
