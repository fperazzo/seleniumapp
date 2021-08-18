from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

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
driver.find_element_by_xpath('//li[contains(@class, "first")]/a[contains(@href, "#tab_patrimonio")]').click()
sleep(2)
trs = driver.find_elements_by_xpath('//div[@class="itens col-60"]/table/tbody/tr')

Acoes = float(trs[0].text.split(" ")[1].replace(".","").replace(",","."))
Fii = float(trs[3].text.split(" ")[1].replace(".","").replace(",","."))
Reits = float(trs[5].text.split(" ")[1].replace(".","").replace(",","."))
Rfixa = float(trs[6].text.split(" ")[2].replace(".","").replace(",","."))
Rvalor = float(trs[7].text.split(" ")[3].replace(".","").replace(",","."))
Stocks = float(trs[8].text.split(" ")[1].replace(".","").replace(",","."))


print("Acoes " + str(Acoes))
print("Fii " + str(Fii))
print("Reits " + str(Reits))
print("Rfixa " + str(Rfixa))
print("Rvalor " + str(Rvalor))
print("Stocks " + str(Stocks))