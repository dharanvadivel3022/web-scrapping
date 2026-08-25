from bs4 import BeautifulSoup
import requests
import csv

url="https://www.amazon.in/ASIAN-Wonder-13-Sports-Running-Shoes/dp/B01N54ZM9W/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.1cd98d97-6013-4b40-a0a0-a663b80c1622&dib=eyJ2IjoiMSJ9.Klh8aAK4J3sROFgBXZT57ZzLs3hi10JTahlHhf7OjMILx92Q-W905NA9uhBLUOk6BD6DP4SlUydxAECt0hCrhpzkBFkez-QKrUwJ6ra6y94p42ilVX8hMVCUYvQ83LRU5QtQ9_OgockEbaoMoY23vqgzWZKH065-Fdn2MleLs3hN_Qxn3b8_X6FJg6c477x4sL69P-_WEK7uMlxgcAXPwEdUfjZFGRlpy9K589GXF1jFkYeubdlANe46XmNvhHs3cct799K7-5dsvfrZjwKlOfJzWBYaf-oyrzaHpSSswBM.So_-p4LUhXSlRctxozkTEVArWOYUMwvpvb5daYcKNbE&dib_tag=se&pd_rd_r=efa83c58-7f25-46ed-8ff3-1959a11e02ac&pd_rd_w=PdAMy&pd_rd_wg=fvapn&qid=1787352089&refinements=p_36%3A-60000&s=shoes&sr=1-1&th=1&psc=1"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"}

response=requests.get(url,headers=header)
if response.status_code==200:
    #print(response.status_code)
    html_content=response.text
else:
    print("Error fetched",response.status_code)

# print(html_content)
soup=BeautifulSoup(html_content,"lxml")

# print(soup.prettify())

product_title=soup.find("div",id="titleSection").text.strip()
product_price=soup.find("span",class_="a-price-whole").text.strip()
product_rating=soup.find("span",class_="a-size-small a-color-base").text.strip()
product_bp=soup.find("ul",class_="a-unordered-list a-vertical a-spacing-small").text.strip()
product_desc=soup.find("div",id="productDescription").text.strip()
reviews=soup.find("ul",id="localTopReviewsList")
unwanted_div=reviews.find("div",class_="a-section")
if unwanted_div:
    unwanted_div.decompose()

product_reviews=reviews.text.strip()

# print(product_title)
# print(product_price)
# print(product_rating)
# print(product_bp)
# print(product_desc)
# print(product_reviews)

with open("Amazon's Asian Running Shoes.csv", mode="w",newline='',encoding='utf-8')as file:
    writer=csv.writer(file)
    writer.writerow(["Product_Title","Product_price","Product_Rating","Product_Bp","Product_desc","Product_Reviews"])
    writer.writerow([product_title,product_price,product_rating,product_bp,product_desc,product_reviews])

print("data Saved")