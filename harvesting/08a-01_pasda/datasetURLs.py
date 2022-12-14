#Purpose: This script will crawl a website and return all of the published dataset landing pages

import csv
import time
import urllib.request
from bs4 import BeautifulSoup


# The site does not have an empty search feature, so we use the keyword value '+' to find all results
resURL = 'https://www.pasda.psu.edu/uci/SearchResults.aspx?Keyword=+'
page = urllib.request.urlopen(resURL).read()
soup = BeautifulSoup(page, 'html.parser')

# table contains all dataset links that start with 'a' html tag
table = soup.find('table', id="DataGrid1")    
hrefs = table.findAll('a')

urls = []
for href in hrefs:
    url = 'https://www.pasda.psu.edu/uci/' + href['href']
    urls.append([url])


# write all dataset urls in csv file with actiondate
actionDate = time.strftime('%Y%m%d')
with open(f'pasdaURLS_{actionDate}.csv', 'w') as fw:
    writer = csv.writer(fw)
    writer.writerows(urls)

