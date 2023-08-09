# Python program to demonstrate
# selenium


from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\geckodriver.exe")
# driver = webdriver.Firefox()
driver.get("https://google.co.in")
