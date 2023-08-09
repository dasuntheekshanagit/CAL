from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time

chrome_path = "C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"
service = Service(chrome_path)

driver = webdriver.Chrome(service=service)

driver.get("https://cal.lk/unittrust/calculator/")


wait = WebDriverWait(driver, 30)

fund_element = wait.until(EC.visibility_of_element_located((By.ID, "funds")))

dropdown = Select(fund_element)
dropdown.select_by_value("IGF")

date_input = driver.find_element(By.ID, "datepicker")
date_input.clear()
desired_date = "2023-05-08" 
date_input.send_keys(desired_date)
date_input.send_keys(Keys.RETURN)

time.sleep(10)

oldprice_element = wait.until(EC.visibility_of_element_located((By.ID, "oldPrice")))
print(oldprice_element.text)


f = open("data.txt", "w+")
f.write(oldprice_element.text+"\n")
f.close()

driver.quit()
