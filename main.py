import requests
from bs4 import BeautifulSoup
import csv # to store data in csv file
# url of website
url="https://en.wikipedia.org/wiki/Artificial_intelligence"
# getting html
con=requests.get(url)
contnt=con.content
sop=BeautifulSoup(contnt,'html.parser')
#print(sop.prettify())
title=sop.title.string   # title  of website

Anc=sop.find_all('a') # finding angle tags (links)
links=set()
for link in Anc:
  if link.get('href')!='#':
    links.add(link)
file='data.csv'
# writing in csv file
with open(file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL"])  # Header row
    writer.writerow([title, url]) 
    
    writer.writerow([]) 
    writer.writerow(["Links"])  # for links

    for link in links:
        writer.writerow([link])

print(f"Data saved to file")