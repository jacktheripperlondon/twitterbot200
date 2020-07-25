from newsapi import NewsApiClient
import requests
from selenium import webdriver
from datetime import datetime,timedelta
from datetime import date
today = date.today()


now = datetime.now()


 
current= now.strftime("%H:%M:%S")
d = now - timedelta(hours=0, minutes=60)
curr2=d.strftime("%H:%M:%S")
times=str(today)+'T'+current
times2=str(today)+'T'+curr2
#keywords = ["hollywood", "movies"]
   
#url = ('https://newsapi.org/v2/top-headlines?q=' + ' OR '.join(keywords)) + '&language=en' +'&from=(today)'+'&to=(times)' + '&apiKey=8e268e93d817478598e019b0351c567a' 
url = 'https://newsapi.org/v2/everything?'
secret='8e268e93d817478598e019b0351c567a'
# Specify the query and number of returns
parameters = {
    'q': 'soya', # query phrase
    'from':times2,
    'to': times,
    'pageSize': 20,  # maximum is 100
    'apiKey': secret # your own API key
}


   
open_page = requests.get(url,params=parameters).json() 
article = open_page["articles"] 
  


results = [] 
  
for ar in article: 
    results.append(ar["url"])


driver = webdriver.Chrome('/home/kali/Downloads/chromedriver')


driver.get("https://twitter.com/login")

driver.implicitly_wait(2)

login=driver.find_element_by_name("session[username_or_email]")
login.send_keys('ichigokurosaki9491868815@gmail.com')
password=driver.find_element_by_name("session[password]")
password.send_keys('incorrect@99')
login_button=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
login_button.click()
driver.implicitly_wait(9)

for j in  range(len(results)):
    
    tweet1=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
    tweet1.click()
    tweet2=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
    
    tweet2.send_keys(results[j])
    driver.implicitly_wait(2)
    tweet3=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
    tweet3.click()
    driver.implicitly_wait(1)    


