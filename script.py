from datetime import datetime

from dbfunctions import inseredg, insereaportes
from scrape_dg import scrapedgerais
from scrape_aportes import scrapeaportes


datanow = datetime.now()

dadosgerais = scrapedgerais(datanow)
inseredg(dadosgerais)

aportes = scrapeaportes(datanow)
inseredg(aportes)


print("importado dados com sucesso : " + datanow.isoformat() )