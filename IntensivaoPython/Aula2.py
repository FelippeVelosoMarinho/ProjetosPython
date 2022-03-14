import pandas as pd #sempre quando for mecher com dados(csv,excel,docs...)

# Passo 1 - Importar a base de dados para o Python
tabela = pd.read_csv("telecom_users.csv")# r no começo serve só quando esta passando o caminho do arquivo

# Passo 2 - Visualizar essa base de dados
# Entender as informações que você tem disponível 
# Descobrir as cagadas da base de dados
# axis = 0 -> linha
# axis = 0 -> coluna
tabela = tabela.drop("Unnamed: 0",axis=1) # nomeDoUqeDeletar,SeEhLinhaOuColuna
print(tabela)

# Passo 3 - Trancamento de Dados
# Analisar se o python está lendo as indormações no formato correto

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # ignore = ignorar, raise = deixar da erro, coerce = transformar em vazio 

# será que existe alguma coluna completamente vazia?
tabela = tabela.dropna(how="all", axis=1) # how = all or any

# será que existe alguma informação em alguma linha vazia?
tabela = tabela.dropna(how="any",axis=0)
# .drop_duplicates() apagar linhas duplicadas
print(tabela.info())

# Passo 4 - Análise Inicial / Análise Global
# quantos clientes cancelaram e quantos não cancelaram
print(tabela["Churn"].value_counts())
# 0 % de clientes que cancelarram e que não cancelaram
#numero = tabela["Churn"].value_counts(normalize=True) * 100
#print(numero)
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))

# Passo 5 -  Análise detalhada (buscar a causa / solição dos cancelamentos)
import plotly.express as px

#coluna = "MesesComoCliente"
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    # exibir o gráfico
    grafico.show()