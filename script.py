from selenium import webdriver
import os
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

#pagina inicial
driver.get('https://www.bastter.com/bs')

sleep(1)
driver.maximize_window()
driver.find_element_by_link_text('Fazer Login').click()
sleep(1)
driver.find_element_by_id('login-email').send_keys('fperazzo')
sleep(1)
driver.find_element_by_id('login-password').send_keys(os.environ.get("PASSBASTTER"))
driver.find_element_by_xpath('//button[text() = "Acessar"]').click()
sleep(5)
driver.find_element_by_xpath('//div[contains(@class, "footer")]/a[contains(@href, "#")]').click()
sleep(2)
driver.find_element_by_xpath('//li[contains(@class, "first active")]/a[contains(@href, "#tab_patrimonio")]').click()
sleep(5)
trs = driver.find_elements_by_xpath('//div[@class="itens col-60"]/table/tbody/tr')
for t in trs:
    print (t.text)