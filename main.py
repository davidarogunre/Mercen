from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from math import floor
from openpyxl import Workbook



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(f'https://www.freelancer.com/freelancers/skills/website-design-mobile-app-development-digital-marketing-web-development')
number_results = driver.find_element('xpath', '//div[@class="result-amount"]')
number_results_text = number_results.text

finalname = []

def get_data(processednamelist, finalname):
            i=0
            while i<len(processednamelist): 
                try:
                    driver.get(f'https://www.freelancer.com/u/{processednamelist[i]}')
                    wait = WebDriverWait(driver, 30)
                    name = wait.until(EC.visibility_of_element_located((By.XPATH, '//h3[@class="ng-star-inserted"]')))
                    finalname.append((name.text, f"https://www.freelancer.com/u/{processednamelist[i]}"))
                    i +=1
                except:
                    i+=1
                    continue
for i in range(1, floor(int(number_results_text.split(" ")[1])/10)+1):
    if i == 1:
        driver.get('https://www.freelancer.com/freelancers/skills/website-design-mobile-app-development-digital-marketing-web-development')
        names = driver.find_elements('xpath','//*[@class="find-freelancer-username"]')


        processednamelist=[i.text for i in names]


        get_data(processednamelist, finalname)

    else:
        driver.get(f'https://www.freelancer.com/freelancers/skills/website-design-mobile-app-development-digital-marketing-web-development/{i}')
        names = driver.find_elements('xpath','//*[@class="find-freelancer-username"]')


        processednamelist=[i.text for i in names]


        get_data(processednamelist, finalname)      
wb = Workbook()
ws = wb.active
ws.title = 'formatting'
def add_data_to_excel():
    ws.append(('Name', 'WebLink'))
    for i in finalname:
        ws.append(i)
    wb.save('data.xlsx')

add_data_to_excel()
