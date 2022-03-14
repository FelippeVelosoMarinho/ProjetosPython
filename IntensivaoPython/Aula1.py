import pyautogui
import pyperclip
import time

#pyautogui -> automatizar o seu mouse, o seu teclado e sua tela
#pypercliip

# escrever o passo a passo em português

pyautogui.PAUSE = 1
# Passo 1 - Entrar no sistema da empresa (no cado o drive)
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter") # botao do teclado

time.sleep(3)

# Passo 2 - Navegar no sistema até encontrar a base de dados
pyautogui.click(x=170, y=272, clicks=2)
time.sleep(2)

# Passo 3 - Exportar a base de vendas
pyautogui.click(x=1108, y=159, clicks=2) # clica no arquivo
#pyautogui.click(x=988, y=724, clicks=2) # clica nos 3 pontinhos
#pyautogui.click(x=988, y=724, clicks=2) # clica em exportar
time.sleep(5) # tempo pra download

# Passo 4 - Calcularia os indicadores (faturamento e quantidade de produtos vendidos)
# pandas , numpy e openpyxL

import pandas as pd

tabela = pd.read_excel(r"C:\Users\felip\Downloads\Python\Exportar\Vendas - Dez.xlsx") #selecionar por abas/colunas "1" ou "nomeDaAba ,sheets("nomedaaba")"
print(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# Passo 5 - Enviar em email para a diretoria com os indicadores
pyautogui.hotkey("ctrl", "t") # abriu uma nova aba
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")# copiou o link
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter") # entrar no site
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=84, y=178)
time.sleep(3)

# escrever destinatário (quem vai receber o email)
pyautogui.write("felippegaloucura@gmail.com")
pyautogui.press("tab")

# escrever o assunto
pyautogui.press("tab") # pular pro campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

# escrever o corpo do e-mail
pyautogui.press("tab") # pula pra campo de corpo do email
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Pipi Poderoso
""" 
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")
