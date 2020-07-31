#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:47:32 2020

@author: kali
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
driver = webdriver.Chrome('/home/kali/Downloads/chromedriver')

driver.get("https://www.agrowon.com/")

driver.implicitly_wait(1)
latest_news=driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div[3]/div/span[1]/a')
latest_news.click()
url=driver.current_url
driver.quit()
results=[]
markup = requests.get(url).text
keywords = ["farm"]


soup = BeautifulSoup(markup, 'html.parser')
links = soup.findAll("a", href=True)
saved_links = []
for link in links:
    for keyword in keywords:
        if keyword in str(link):
            saved_links.append(link["href"])
for i in saved_links:
    lin=url+i
    results.append(lin)
                
result1=set(results)
result=list(result1)          
# if(len(result)!=0):
#     driver = webdriver.Chrome('/home/kali/Downloads/chromedriver')

#     driver.get("https://twitter.com/login")
    
#     driver.implicitly_wait(100)

#     login=driver.find_element_by_name("session[username_or_email]")
#     login.send_keys('ichigokurosaki9491868815@gmail.com')
#     password=driver.find_element_by_name("session[password]")
#     password.send_keys('incorrect@99')
#     login_button=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
#     login_button.click()
#     driver.implicitly_wait(3)
    
#     for j in  range(len(result)):
        
#         tweet1=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
#         tweet1.click()
#         tweet2=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        
#         tweet2.send_keys(result[j])
#         driver.implicitly_wait(2)
#         tweet3=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
#         tweet3.click()
#         driver.implicitly_wait(1)    
#     driver.quit()    
# else:
#     sys.exit()    
