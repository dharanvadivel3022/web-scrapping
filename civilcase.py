from bs4 import BeautifulSoup
import requests

url='https://fcdcfcjs.co.franklin.oh.us/CaseInformationOnline/caseSearch?gg5pX2IiQxSetC0oorzR'
header={'User-Agent':'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'}
session=requests.session()
response=requests.post(url,headers=header)
if response.status_code==200:
    #print(response.status_code)
    source_code=response.text
    soup=BeautifulSoup(response.text,'lxml')
    #print(soup.prettify())
    table = soup.find('table', id='main')
    if table is None:
        print("Table not found")
        with open("ccd.html", "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        row = table.find('tr')
        headers = [h.get_text(strip=True) for h in row.find_all('th')]
        print(headers)
else:
    print("Connection Failed",response.status_code)