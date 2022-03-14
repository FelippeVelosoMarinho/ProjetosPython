# selenium permite controlar o navegador de forma automática
# instalar o chrome driver https://chromedriver.chromium.org/downloads
#!pip install selenium

from selenium import webdriver # controlar o navegador
from selenium.webdriver.common.keys import Keys # controlar o teclado
from selenium.webdriver.common.by import By # Localizar os items no navegador

#cria o navegador
navegador = webdriver.Chrome()

# entraria no google e pesquisaria por cotação do dólar
navegador.get("https://www.google.com/")

# pegaria a cotação do dólar - clica no elemento do campo de busca e escreve "cotação dólar"
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
print(cotacao_dolar)

# entraria no google e pesquisaria a cotação do euro
navegador.get("https://www.google.com/")

navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") 
print(cotacao_euro)

# entraria no site https://www.melhorcambio.com/ouro-hoje
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute("value") 
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

navegador.quit()


# importar a base de dados
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# atualizar as cotações na base de dados
# atualizar o preço de compra e de venda na base de dados

# atualizar a cotação
# nas linhas onde na coluna "Moeda" = Dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar o preço base reais (preço base original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# atualizar o preço final (preço base reais * Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)

print(tabela)

# exportar essa base de dados para ter o resultado atualizado
tabela.to_excel("Produtos Novo.xlsx", index=False)