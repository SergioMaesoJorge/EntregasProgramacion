import pandas as pd
import matplotlib.pyplot as plt
def a():
    datos=pd.read_csv('Clasificacion.csv')
    df=datos[['NOM_EMS','SUPERFICIE','TIPUSSOL','CODI_TIPUSSOL']]
    df.plot.scatter(x='SUPERFICIE',y='TIPUSSOL', alpha=0.3)
    plt.show()
a()