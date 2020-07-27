#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:30:50 2020

@author: kali
"""

from newsapi import NewsApiClient
import requests
from selenium import webdriver
from datetime import timedelta
# from datetime import date
import datetime



current_date = datetime.datetime.now()
to_date = current_date.strftime('%Y-%m-%dT%H:%M:%SZ')

from_date = (current_date - timedelta(hours=12)).strftime('%Y-%m-%dT%H:%M:%SZ')





   
keys=["soy","Soy","SOY","SOYBEAN","Soybean","soybean"]
url = 'https://newsapi.org/v2/everything?'
secret='8e268e93d817478598e019b0351c567a'
#Specify the query and number of returns
parameters = {
    
    'q':'soy OR Dog',
    'from': from_date,
    'to':to_date,
    'language':'en',
    'pageSize': 60,  # maximum is 100
    'apiKey': secret # your own API key
}
#url='https://newsapi.org/v2/top-headlines?country=in&q=sales&from=(from_date)&apiKey=8e268e93d817478598e019b0351c567a'


   
open_page = requests.get(url,params=parameters).json() 
article = open_page["articles"] 
  


results = [] 
  
for ar in article: 
    results.append(ar["url"])
if(len(results)!=0):
        driver = webdriver.Chrome('/home/kali/Downloads/chromedriver')
    
        driver.get("https://twitter.com/login")
        
        driver.implicitly_wait(100)
    
        login=driver.find_element_by_name("session[username_or_email]")
        login.send_keys('ichigokurosaki9491868815@gmail.com')
        password=driver.find_element_by_name("session[password]")
        password.send_keys('incorrect@99')
        login_button=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
        login_button.click()
        driver.implicitly_wait(3)
        
        for j in  range(len(results)):
            
            tweet1=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
            tweet1.click()
            tweet2=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
            
            tweet2.send_keys(results[j])
            driver.implicitly_wait(2)
            tweet3=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
            tweet3.click()
            driver.implicitly_wait(1)    

#print(open_page)    
