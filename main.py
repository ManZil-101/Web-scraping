
from csv import writer
from wsgiref import headers
from bs4 import BeautifulSoup
import requests



html_text=requests.get('https://www.jobsnepal.com/').text
soup = BeautifulSoup(html_text, 'lxml')
jobs= soup.find_all('div', class_='col-sm-6 col-md-6 col-lg-4 mb-3')

with open('data4.csv','w', encoding='utf8', newline='') as f:
    the_writer = writer(f)
    header = ['Title', 'Company Name', 'location', 'link']
    the_writer.writerow(header)

    for job in jobs:
        job_title = job.find('div', class_='card-body')
        title = job_title.h2['title']
        #company_name= jobs.find('h3').text
        company_name=job.h3.a.text.replace("\n","")
        company_link= job.h3.a['href']
        location = job.span.text.replace("\n","")

        info=[title, company_name,location,company_link]
        the_writer.writerow(info)

