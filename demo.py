#Case number , Type of case , status , DAte filed , Courtroom , judge should stop at 5 no case match and continue tomorrow afterwards





from bs4 import BeautifulSoup
import requests

url='https://fcdcfcjs.co.franklin.oh.us/CaseInformationOnline/caseSearch?XkQWEBNZ4xZGXvLKtHXX'
header={'User-Agent':'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36'}
session= requests.session()
session.get('https://fcdcfcjs.co.franklin.oh.us/CaseInformationOnline/caseSearch?XkQWEBNZ4xZGXvLKtHXX')
payload = {
    "caseYear": "26",
    "caseType": "CV",
    "caseSeq": "000001",
}

response=session.post(url,data=payload)
if response.status_code==200:
    print(response.status_code)
    soup=BeautifulSoup(response.text,'lxml')
    print(soup.prettify())


else:
    print('Nothing')










