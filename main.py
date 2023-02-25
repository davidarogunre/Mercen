from selenium import webdriver
import time
import asyncio
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
finalname = []

for i in range(1, 12):
    if i == 1:
        driver.get('https://www.freelancer.com/freelancers')
        names = driver.find_elements('xpath','//*[@class="find-freelancer-username"]')
        wait = WebDriverWait(driver, 30)


        processednamelist=[i.text for i in names]

        def get_data():
            i=0
            while i<len(processednamelist): 
                driver.get(f'https://www.freelancer.com/u/{processednamelist[i]}')
                name = wait.until(EC.presence_of_element_located((By.XPATH, '//h3[@class="ng-star-inserted"]')))
                finalname.append({"name": name.text, "weblink":f"https://www.freelancer.com/u/{processednamelist[i]}"})
                i +=1

        get_data()

    else:
        driver.get(f'https://www.freelancer.com/freelancers/{i}')
        names = driver.find_elements('xpath','//*[@class="find-freelancer-username"]')


        processednamelist=[i.text for i in names]

        def get_data():
            i=0
            while i<len(processednamelist): 
                driver.get(f'https://www.freelancer.com/u/{processednamelist[i]}')
                wait = WebDriverWait(driver, 30)
                name = wait.until(EC.presence_of_element_located((By.XPATH, '//h3[@class="ng-star-inserted"]')))
                finalname.append({"name": name.text, "weblink":f"https://www.freelancer.com/u/{processednamelist[i]}"})
                i +=1

        get_data()      

print(finalname)