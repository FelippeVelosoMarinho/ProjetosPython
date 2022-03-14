import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("advertising.csv")
print(tabela)

#cria grafico - vários tipo no site scatterplot matrix seaborn biblioteca
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
#exibe grafico
plt.show()

y = tabela["Vendas"]
x = tabela[["TV", "Radio", "Jornal"]]

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1) # treina aleatóriaente sua inteligência artificial / randomstate limita a aleatoriedade, portanto pra treiná-la realmente, tem que tirar

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# criar os modelos - "criar inteligência artificial"
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treinar os modelos - "treinar inteligência artificial"
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn import metrics

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

# arvore de decisão é o melhor modelo

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

# importar outra tabela com novas informações que vc quer prever

nova_tabela = pd.read_csv("novos.csv")
display(nova_tabela)

# usar o modelo_arvoredecisao e fazer um.predict com ele
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()

# Caso queira comparar Radio com Jornal
# print(df[["Radio", "Jornal"]].sum())