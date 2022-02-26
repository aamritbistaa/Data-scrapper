from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import requests
import csv
import pandas as pd




def wait(self):
    time.sleep(self)

#KEY=input("Enter company name:  ")
KEY="idbl"
wait(3)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait(1)
url="https://www.sharesansar.com/"
wait(1)
driver.maximize_window()

driver.get(url)
wait(1)



#<input id="company_search" class="form-control" placeholder="Company Name or Symbol" autocomplete="off">
element=driver.find_element(By.CLASS_NAME,"form-control")
# element=driver.find_element(By.ID,"company_name")
element.click()
wait(1)
element.send_keys(KEY)
wait(1)
element.send_keys(Keys.ENTER)

companyName=driver.find_element(By.CLASS_NAME,"heading-title")
print(companyName.text)

#selecting price history button
priceHistory=driver.find_element(By.ID,"btn_cpricehistory")
priceHistory.click()

wait(1)


# <select name="" aria-controls="myTableCPriceHistory" class=""><option value="10">10</option><option value="20">20</option><option value="50">50</option></select>
select = Select(driver.find_element(By.NAME,"myTableCPriceHistory_length"))

# select by visible text
select.select_by_visible_text('50')

wait(1)

tableHeading=driver.find_element(By.XPATH,'//*[@id="myTableCPriceHistory"]/thead')
print(tableHeading.text)

while(1):
    #table_data=driver.find_elements(By.XPATH,'//table[@id="myTableCPriceHistory"]')
    tableData=driver.find_elements(By.XPATH,'//*[@id="myTableCPriceHistory"]/tbody')
    for tableData in tableData:
    #    print(tableData.text)

        print(tableData[0])



    driver.find_element(By.XPATH,'//*[@id="myTableCPriceHistory_next"]').click()

   
    #<a class="paginate_button next disabled" aria-controls="myTableCPriceHistory" data-dt-idx="7" tabindex="0" id="myTableCPriceHistory_next">Next</a>
    wait(1)


# <a class="paginate_button next" aria-controls="myTableCPriceHistory" data-dt-idx="7" tabindex="0" id="myTableCPriceHistory_next">Next</a>

print("End of file")

driver.close()