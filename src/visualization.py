import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_portfolio_performance(data):
    data.plot(figsize=(10,6))
    plt.title('Výkonnost All-Weather Portfolia oproti S&P 500')
    plt.xlabel('Datum')
    plt.ylabel('Hodnota portfolia')
    plt.show()

def plot_correlation(data):
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Korelace mezi jednotlivými aktivy')
    plt.show()

# Příklad načtení dat a vykreslení grafu
data = pd.read_csv('data/all_weather.csv', index_col='Datum', parse_dates=True)
plot_portfolio_performance(data)