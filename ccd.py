from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://fcdcfcjs.co.franklin.oh.us/CaseInformationOnline/caseSearch?XkQWEBNZ4xZGXvLKtHXX")

driver.find_element(By.NAME, "caseYear").send_keys("26")
driver.find_element(By.NAME, "caseType").send_keys("CV")
driver.find_element(By.NAME, "caseSeq").send_keys("000001")
driver.find_element(By.NAME, "reallySubmit").click()


from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')