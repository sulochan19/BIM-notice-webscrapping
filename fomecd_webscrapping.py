import csv
from bs4 import BeautifulSoup
import requests

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.fomecd.edu.np/index.php?level=b')
html=driver.page_source



soup=BeautifulSoup(html,'html.parser')

csv_file=open('fomecd.csv','a',encoding="utf-8")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['published date','description','link to pdf','link details'])


for total_notices in soup.find_all('div',class_='noticeslist'):
    # print(total_notices.prettify())
    for notices in total_notices.find_all('div',class_=None):
        date=notices.label.text

        # print(date)


        description = notices.label.next_sibling
        # print(description)

        try:
            pdf_description = notices.span.a.text
            # print(pdf_description, end="      ")
        except Exception as e:
            pdf_description = "not available"
            # print(pdf_description,end="      ")

        try:
            link=notices.span.a['href']
            # print(link)
        except Exception as e:
            link="not available"
            # print(link)
        if 'BIM' in description:
            print(date,description,pdf_description,link)
            # csv_writer.writerow([date,description,link,pdf_description])
driver.quit()


# "https://www.fomecd.edu.np/"+