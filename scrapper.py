from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd




def wait(self):
    time.sleep(self)
#KEY=input("Enter company name:  ")
print("The data is extracted from https://www.sharesansar.com/")
print("Each page should have 50 data entries")
KEY=input("Enter company Name or Symbol: ")
PAGENO=int(input("Enter total number of page: "))

wait(3)
#PATH = "C:\Users\thebalanar\Desktop\Data scrapper\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome()
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
table_data_list=[]
for i in range(0,PAGENO):
    table_data=driver.find_elements(By.XPATH,'//table[@id="myTableCPriceHistory"]')
    tableData=driver.find_elements(By.XPATH,'//*[@id="myTableCPriceHistory"]/tbody')
    for tableiData in tableData:
        #print(tableiData.text)
        c = tableiData.text
        table_data_list.append(c)
#         textfile = open("a_file.txt", "a")
#         textfile.write(c + "\n")
#         textfile.close()
        
    if i==PAGENO-1:
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="myTableCPriceHistory_next"]').click()

   
    #<a class="paginate_button next disabled" aria-controls="myTableCPriceHistory" data-dt-idx="7" tabindex="0" id="myTableCPriceHistory_next">Next</a>
    wait(1)


# <a class="paginate_button next" aria-controls="myTableCPriceHistory" data-dt-idx="7" tabindex="0" id="myTableCPriceHistory_next">Next</a>

print("End of file")

driver.close()


z=[]
for i in range(0,PAGENO):
    cdd = table_data_list[i].split("\n")
    for item in cdd:
        cdd_s = item.split(" ")
        z.append(list(cdd_s))
        
df = pd.DataFrame(z, columns =['SN', 'Date',"Open","HIGH","lOW","LTP","%change","Qty","Turnover"])

SF = df.to_csv(f"Data\{KEY}.csv")
print("Data saved")