import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import re

workbook = load_workbook('info.xlsx')
worksheet = workbook.active

with open('urls.txt') as f:
    row_num = 1
    for line in f:
        page = requests.get(line.strip('\n'))
        content = page.text
        scraper  = BeautifulSoup(page.content, 'html.parser')
        body = scraper.body

        name = scraper.find('b').text
        phone_numbers = list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", content))
        emails = list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", content))

        worksheet.cell(row=row_num, column=1, value=name)
        worksheet.cell(row=row_num, column=2, value=phone_numbers[0])
        worksheet.cell(row=row_num, column=3, value=emails[0])
        row_num+=1

workbook.save('info.xlsx')
