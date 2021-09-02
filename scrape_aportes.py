from selenium import webdriver
import os
from time import sleep
from datetime import date, datetime
from dbfunctions import inseredg


def scrapeaportes(dataagora):

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
    driver.find_element_by_id('login-password').send_keys('Trezedo07')
    driver.find_element_by_xpath('//button[text() = "Acessar"]').click()
    sleep(5)
    driver.find_element_by_xpath('//div[contains(@class, "footer")]/a[contains(@href, "#")]').click()
    sleep(2)
    driver.find_element_by_xpath('//a[contains(@href, "#tab_financeiro")]').click()
    sleep(2)
    trs_aporte = driver.find_elements_by_xpath('//div[@class="consolidado"]/table/tbody/tr')

    dados = []
    Acoes = 0
    Fii = 0
    Reits = 0
    Rfixa = 0
    Rvalor = 0
    Stocks = 0

    for tt in trs_aporte:
        try:
            a = float(tt.text.split(" ")[0])
            a = tt.text.split(" ")[1]
        except:
            a = tt.text.split(" ")[0]


        if a == "Renda":
            tp = "Renda Fixa"
        else:
            if a == "Reserva":
                tp = "Reserva de Valor"
            else:
                tp = a

        valor = tt.text.replace(tp+" ","").split(" ")

        if len(valor)>1:
            valor = valor[1]
        else:
            valor = valor[0]

        valor =valor.replace(".","").replace(",",".")

        if tp == "Ação":
            Acoes = Acoes + round(valor,2)
        if tp == "FII":
            Fii = Fii + round(valor,2)
        if tp == "REIT":
            Reits = Reits + round(valor,2)
        if tp == "Renda Fixa":
            Rfixa = Rfixa + round(valor,2)
        if tp == "Reserva de Valor":
            Rvalor = Rvalor + round(valor,2)
        if tp == "Stock":
            Stocks = Stocks + round(valor,2)

    dados = [(dataagora,Acoes,Fii,Reits,Rfixa,Rvalor,Stocks)]

    driver.close()

    return dados