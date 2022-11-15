import pandas as pd
import matplotlib.pyplot as plt
def consumirHistograma():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']]
    df.RM.plot.hist()
    plt.show()
#consumir()
def consumirDispersion():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']]
    df.plot.scatter(x='CRIM', y='MEDV',alpha=0.8)
    plt.show()
#consumirDispersion()
def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']]
    valor_por_ciudad = df.groupby("TOWN")["MEDV"].mean()
    valor_por_ciudad.head(5).plot.barh()
    plt.show()
    df[""]
#consumirBarras()
def consumirCajas():
    datos=pd.read_csv('casasboston.csv')
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    df.head(10).boxplot(column="MEDV",by="TOWN",figsize=(8,6))
    plt.show()
#consumirCajas()
def consumirCircular():
    datos=pd.read_csv('casasboston.csv')
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    df.CRIM.head(10).value_counts().plot.pie()
    plt.show()
consumirCircular()