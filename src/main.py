import urllib3
from bs4 import BeautifulSoup
import requests
http = urllib3.PoolManager()

link = "http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm"
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36'}

response = http.request('GET', link, headers=headers)
soup = BeautifulSoup(response.data,'html.parser')
strhtm = soup.prettify()
