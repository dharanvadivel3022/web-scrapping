#name location price ratings reviews link
import random

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv
import time


#url="https://www.oyorooms.com/search?location=Mumbai%2C%20Maharashtra%2C%20India&city=Mumbai&searchType=city&checkin=25%2F08%2F2026&checkout=26%2F08%2F2026&roomConfig%5B%5D=1&guests=1&rooms=1&filters%5Bcity_id%5D=5"
header={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
base_url="https://www.oyorooms.com"



def web_scrapping(url,f_nane):
    print("Wait for a moment")
    num=random.randint(4,8)
    time.sleep(num)
    response = requests.get(url, headers=header)

    if response.status_code==200:
        print("Connected to the Website")
        html_content = response.text
        soup=BeautifulSoup(html_content,"lxml")

        hotel_num=soup.find_all('div', class_="oyo-cell--12-col oyo-cell--8-col-tablet oyo-cell--4-col-phone")
        with open(f'{f_nane}.csv','w',encoding='utf-8',newline='') as file_csv:
            writer=csv.writer(file_csv)
            writer.writerow(['Hotel Name','Location','Price','Ratings','No. of Ratings','Links'])


            for hotel in hotel_num:
               hotel_name=hotel.find('h3',class_="listingHotelDescription__hotelName d-textEllipsis").text.strip()
               location=hotel.find('div',class_="d-body-lg listingHotelDescription__hotelAddress").text.strip()
               price=hotel.find('span', class_="listingPrice__finalPrice listingPrice__finalPrice--black").text.strip()
               ratings = hotel.find_all('div',class_="hotelRating")
               for scores in ratings:
                   rat = scores.find('span').text.strip()
                   rat if rat else 'NA'
               no_of_rat = hotel.find('span', class_='hotelRating__ratingSummary').text.strip()
               no_of_rat if no_of_rat else 'NA'
               link=hotel.find('a',href=True).get('href')
               full_link=urljoin(base_url,link)
               writer.writerow([hotel_name,location,price,rat,no_of_rat,full_link])



            # print(hotel_name)
            # print(location)
            # print(price)
            #
            # print(rat)
            # print(no_of_rat)
            # print(full_link)
            #
            #
            # print('')
        # print(soup.prettify())
        print("Web Scrapping Completed")

    else:
        print("Error Fetched",response.status_code)

if __name__=='__main__':
    url=input("Please Enter the URL:")
    fn=input("Enter the file name:")
    web_scrapping(url,fn)

