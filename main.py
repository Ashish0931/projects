import bs4 as bs
import requests
import os
from selenium import webdriver
import urllib.request
import time
import ast
import urllib.request as ulib
from bs4 import BeautifulSoup as bs
word=input(" for what do you want to download images for?")
print("-------------------------------")
driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.com/search?tbm=isch&q='+word)
i=0
num=int(input("enter the number of images you want"))
while i<2:
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    try:
        # for clicking show more results button
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(2)
    i += 1
print("=============================================================")
soup = bs(driver.page_source, 'html.parser')
driver.close()
img_tags = soup.find_all("img", class_="rg_i")
tags=[]
for i in img_tags:
    tags.append(i)
count=0
for j in range (num):
    try:
        # passing image urls one by one and downloading
        urllib.request.urlretrieve(tags[j]['src'], str(count) + ".jpg")
        count += 1
        print("Number of images downloaded = " + str(count), end='\r')
    except Exception as e:
        pass

