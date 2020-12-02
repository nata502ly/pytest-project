from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys('Natalia Roshchyna')
time.sleep(5)

optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

print(len(optionsList))
for el in optionsList:
    print(el.text)
    if el.text == 'наталья рощина все книги':
        el.click()
        break

time.sleep(5)

driver.close()