import csv
import re
import csv
from urllib.request import urlopen


from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('output14d-01-02.csv', 'w'))
f.writerow(['url','Title','JPEG','PDF','Rights','DOI'])

with open('14d-01-02.csv','r') as harvest:
     urls = csv.reader(harvest)
     for url in urls:
        portalMetadata.append(url)

for url in portalMetadata:
      page = urlopen(url[0]).read()
      soup = BeautifulSoup(page, "html.parser")
      
      pageLink =str(url)[1:-1]
      
      titleField = soup.find(attrs={'id': 'contentTitle'})
      title = titleField.text.strip()
      
      
      try:
            jpegField = soup.find('a', href=True, text="JPEG-1")
            jpeg = jpegField['href']
      except:
            jpeg = ''
      
      try:
            pdfField = soup.find('a', href=True, text="PDF-1")
            pdf = pdfField['href']
      except:
            pdf = ''
      
      try:
            rightsField = soup.find(attrs={'class': 'resultFull__result-title'}, text="Rights").next_sibling
            rights = rightsField.text.strip()
      except:
            rights = ''
      
      try:
            doiField = soup.find(attrs={'class': 'resultFull__result-title'}, text="Persistent URL").next_sibling
            doi = doiField.text.strip()
      except:
            doi = ''
      
      
      
      
      f.writerow([pageLink,title,jpeg,pdf,rights,doi])
      
      
      
#       rightsField = soup.find(attrs={'id': 'RIGHTS1'}).contents[3]
#       rights =rightsField.text.strip()

#       titleField = soup.title.name
#       title = titleField

# 	title = titleField.text.strip()

# 	titleField = soup.find(attrs={'id': 'RIGHTS1'})



# 	titleField = soup.find(attrs={'class': 'description'})
# 	dateField = soup.find(attrs={'id': 'Label2'})
# 	publisherField = soup.find(attrs={'id': 'Label3'})
# 	descriptionField = soup.find(attrs={'id': 'Label14'})
# 	metadataLink = soup.find('a', href=True, text='Metadata')



# 	date = dateField.text.strip(),
# 	publisher = publisherField.text.strip(),
# 	description = descriptionField.text.strip(),
# 	metadata = metadataLink['href'],


















