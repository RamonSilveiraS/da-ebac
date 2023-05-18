import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dados = pd.read_csv('gasolina.csv')

sns.set_style="whitegrid"  
sns.color_palette("pastel")

sns.lineplot(x='dia', y='venda', data=dados, color='red')
plt.title('Preço por dia')

plt.savefig('gasolina.png')