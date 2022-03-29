from turtle import title
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.naukri.com/2022-jobs?cityTypeGid=97&industryTypeIdGid=109' 
#page = requests.get(url)
# print(page.text)


                           
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(url)
time.sleep(3)
soup = BeautifulSoup(driver.page_source,'html5lib')
# print(soup.prettify())
driver.close()

results = soup.find(class_='list')
print(list)

URLs=[]
job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')
for job_elem in job_elems:
    URL = job_elem.find('a',class_='title fw500 ellipsis').get('href')
    URLs.append(URL)
    print(URLs)
    
print('********************************************')
    
    
    
title=soup.find_all('a',class_='title fw500 ellipsis')
titles=[]
for i in range(0,len(title)):
        titles.append(title[i].get_text())
print(titles) 
print('********************************************')

company=soup.find_all('a',class_='subTitle ellipsis fleft')
COM=[]
for i in range(0,len(company)):
        COM.append(company[i].get_text())
print(COM) 

print('********************************************')

description=soup.find_all('div',class_='job-description fs12 grey-text')
DES=[]
for i in range(0,len(description)):
        DES.append(description[i].get_text())
print(DES) 
 
print('********************************************')

experince=soup.find_all('li',class_='fleft grey-text br2 placeHolderLi experience')
EXP=[]
for i in range(0,len(experince)):
        EXP.append(experince[i].get_text())
print(EXP) 

print('********************************************')

salary=soup.find_all('li',class_='fleft grey-text br2 placeHolderLi salary')
SAL=[]
for i in range(0,len(salary)):
        SAL.append(salary[i].get_text())
print(SAL) 

print('********************************************')

location=soup.find_all('li',class_='fleft grey-text br2 placeHolderLi location')
LOC=[]
for i in range(0,len(location)):
        LOC.append(location[i].get_text())
print(LOC) 

scraped_data = pd.DataFrame({'URL': URLs, 
'TITLES': titles, 'COMPANY': COM,
'DESCRIPTION': description,'EXPERIENCE': experince,'SALARY': salary,
'LOCATION': LOC})

scraped_data.to_csv('job_details.csv', index=False)