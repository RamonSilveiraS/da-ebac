import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dados = pd.read_csv('gasolina.csv')

sns.set(style="darkgrid")  

sns.lineplot(x='dia', y='venda', data=dados)

plt.show()