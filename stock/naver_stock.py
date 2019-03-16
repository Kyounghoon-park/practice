from urllib.request import urlopen
from bs4 import BeautifulSoap

url = 'https://finace.naver.com/sise/'
page = urlopen(url)
#print(soap.pretify())
kospi = soup.find('span', id='KOSPI_now')
print(kospi.string)