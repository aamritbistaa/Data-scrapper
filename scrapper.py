from cgitb import html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import requests
import csv




def wait(self):
    time.sleep(self)

KEY=input("Enter company name:  ")
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
wait(1)

#table information
# <table id="myTableCPriceHistory" class="table table-hover table-striped table-bordered compact dataTable no-footer" role="grid" aria-describedby="myTableCPriceHistory_info">
#                                         <thead class="bg-danger">
#                                         <tr role="row"><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="S.N." style="width: 4%;">S.N.</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Date" style="width: 10%;">Date</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Open" style="width: 10%;">Open</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="High" style="width: 10%;">High</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Low" style="width: 10%;">Low</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Ltp" style="width: 10%;">Ltp</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="% Change" style="width: 10%;">% Change</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Qty" style="width: 18%;">Qty</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Turnover" style="width: 18%;">Turnover</th></tr></thead>
#                                         <tbody>ger-index">804.00</td><td class="danger-index">804.00</td><td class="danger-index">785.00</td><td class="danger-index">790.00</td><td class="danger-index">-1.74</td><td class="danger-index">62,153.00</td><td class="danger-index">49,201,909.50</td></tr><tr role="row" class="even"><td class="danger-index">2</td><td class="danger-index">2022-02-23</td><td class="danger-index">810.00</td><td class="danger-index">810.00</td><td class="danger-index">801.00</td><td class="danger-index">804.00</td><td class="danger-index">-0.50</td><td class="danger-index">26,347.00</td><td class="danger-index">21,165,563.70</td></tr><tr role="row" class="odd"><td class="success-index">3</td><td class="success-index">2022-02-22</td><td class="success-index">806.00</td><td class="success-index">815.00</td><td class="success-index">802.00</td><td class="success-index">808.00</td><td class="success-index">0.24</td><td class="success-index">37,501.00</td><td class="success-index">30,314,745.80</td></tr><tr role="row" class="even"><td class="success-index">4</td><td class="success-index">2022-02-21</td><td class="success-index">808.00</td><td class="success-index">810.00</td><td class="success-index">798.00</td><td class="success-index">806.10</td><td class="success-index">0.37</td><td class="success-index">30,102.00</td><td class="success-index">24,132,081.90</td></tr><tr role="row" class="odd"><td class="danger-index">5</td><td class="danger-index">2022-02-20</td><td class="danger-index">799.70</td><td class="danger-index">812.00</td><td class="danger-index">790.00</td><td class="danger-index">803.10</td><td class="danger-index">-1.58</td><td class="danger-index">58,816.00</td><td class="danger-index">47,104,309.40</td></tr><tr role="row" class="even"><td class="success-index">6</td><td class="success-index">2022-02-17</td><td class="success-index">805.00</td><td class="success-index">816.00</td><td class="success-index">804.00</td><td class="success-index">816.00</td><td class="success-index">1.12</td><td class="success-index">55,936.00</td><td class="success-index">45,273,568.40</td></tr><tr role="row" class="odd"><td class="success-index">7</td><td class="success-index">2022-02-16</td><td class="success-index">806.00</td><td class="success-index">815.00</td><td class="success-index">803.00</td><td class="success-index">807.00</td><td class="success-index">0.25</td><td class="success-index">43,171.00</td><td class="success-index">34,835,752.90</td></tr><tr role="row" class="even"><td class="primary-index">8</td><td class="primary-index">2022-02-15</td><td class="primary-index">805.00</td><td class="primary-index">810.00</td><td class="primary-index">802.00</td><td class="primary-index">805.00</td><td class="primary-index">0.00</td><td class="primary-index">45,673.00</td><td class="primary-index">36,821,646.30</td></tr><tr role="row" class="odd"><td class="danger-index">9</td><td class="danger-index">2022-02-14</td><td class="danger-index">811.00</td><td class="danger-index">814.00</td><td class="danger-index">798.00</td><td class="danger-index">805.00</td><td class="danger-index">-0.25</td><td class="danger-index">65,371.00</td><td class="danger-index">52,459,382.00</td></tr><tr role="row" class="even"><td class="danger-index">10</td><td class="danger-index">2022-02-13</td><td class="danger-index">802.00</td><td class="danger-index">811.00</td><td class="danger-index">789.00</td><td class="danger-index">807.00</td><td class="danger-index">-1.34</td><td class="danger-index">180,844.00</td><td class="danger-index">144,338,091.70</td></tr><tr role="row" class="odd"><td class="danger-index">11</td><td class="danger-index">2022-02-10</td><td class="danger-index">830.00</td><td class="danger-index">839.00</td><td class="danger-index">814.00</td><td class="danger-index">818.00</td><td class="danger-index">-1.21</td><td class="danger-index">95,660.00</td><td class="danger-index">78,333,501.40</td></tr><tr role="row" class="even"><td class="danger-index">12</td><td class="danger-index">2022-02-09</td><td class="danger-index">840.00</td><td class="danger-index">840.00</td><td class="danger-index">821.00</td><td class="danger-index">828.00</td><td class="danger-index">-1.08</td><td class="danger-index">87,317.00</td><td class="danger-index">72,331,456.20</td></tr><tr role="row" class="odd"><td class="danger-index">13</td><td class="danger-index">2022-02-08</td><td class="danger-index">855.00</td><td class="danger-index">872.00</td><td class="danger-index">826.00</td><td class="danger-index">837.00</td><td class="danger-index">-0.71</td><td class="danger-index">86,778.00</td><td class="danger-index">72,856,295.00</td></tr><tr role="row" class="even"><td class="danger-index">14</td><td class="danger-index">2022-02-07</td><td class="danger-index">853.00</td><td class="danger-index">858.00</td><td class="danger-index">839.00</td><td class="danger-index">843.00</td><td class="danger-index">-1.17</td><td class="danger-index">59,770.00</td><td class="danger-index">50,503,450.30</td></tr><tr role="row" class="odd"><td class="danger-index">15</td><td class="danger-index">2022-02-06</td><td class="danger-index">856.00</td><td class="danger-index">860.00</td><td class="danger-index">845.00</td><td class="danger-index">853.00</td><td class="danger-index">-0.86</td><td class="danger-index">72,123.00</td><td class="danger-index">61,459,588.40</td></tr><tr role="row" class="even"><td class="danger-index">16</td><td class="danger-index">2022-02-03</td><td class="danger-index">870.00</td><td class="danger-index">877.00</td><td class="danger-index">860.00</td><td class="danger-index">860.40</td><td class="danger-index">-1.10</td><td class="danger-index">150,826.00</td><td class="danger-index">130,653,042.50</td></tr><tr role="row" class="odd"><td class="danger-index">17</td><td class="danger-index">2022-02-01</td><td class="danger-index">875.00</td><td class="danger-index">883.00</td><td class="danger-index">865.00</td><td class="danger-index">870.00</td><td class="danger-index">-0.23</td><td class="danger-index">58,118.00</td><td class="danger-index">50,707,160.60</td></tr><tr role="row" class="even"><td class="danger-index">18</td><td class="danger-index">2022-01-31</td><td class="danger-index">890.00</td><td class="danger-index">890.00</td><td class="danger-index">870.10</td><td class="danger-index">872.00</td><td class="danger-index">-1.25</td><td class="danger-index">65,157.00</td><td class="danger-index">57,041,932.30</td></tr><tr role="row" class="odd"><td class="success-index">19</td><td class="success-index">2022-01-30</td><td class="success-index">876.70</td><td class="success-index">888.00</td><td class="success-index">872.00</td><td class="success-index">883.00</td><td class="success-index">2.72</td><td class="success-index">99,204.00</td><td class="success-index">87,055,768.70</td></tr><tr role="row" class="even"><td class="danger-index">20</td><td class="danger-index">2022-01-27</td><td class="danger-index">861.00</td><td class="danger-index">869.90</td><td class="danger-index">856.00</td><td class="danger-index">859.60</td><td class="danger-index">-0.05</td><td class="danger-index">56,260.00</td><td class="danger-index">48,363,360.90</td></tr></tbody>
#                                         <tr role="row" class="odd"><td class="danger-index">1</td><td class="danger-index">2022-02-24</td><td class="dan
#                                     </table>

while(1):
    #table_data=driver.find_elements(By.XPATH,'//table[@id="myTableCPriceHistory"]')
    tableData=driver.find_elements(By.XPATH,'//*[@id="myTableCPriceHistory"]/tbody')
    for tableData in tableData:
        print(tableData.text)

    driver.find_element(By.XPATH,'//*[@id="myTableCPriceHistory_next"]').click()
   


# <a class="paginate_button next disabled" aria-controls="myTableCPriceHistory" data-dt-idx="7" tabindex="0" id="myTableCPriceHistory_next">Next</a>
    wait(2)

driver.close()