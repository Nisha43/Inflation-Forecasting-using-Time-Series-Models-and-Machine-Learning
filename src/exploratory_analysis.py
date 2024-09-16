import matplotlib.pyplot as plt

def plot_inflation_trend(data, country_name):
    country_data = data[data['Country Name'] == country_name]
    plt.plot(country_data.columns[4:], country_data.iloc[0, 4:], label='Inflation Rate')
    plt.title(f'Inflation Rate in {country_name} Over Time')
    plt.xlabel('Year')
    plt.ylabel('Inflation Rate (%)')
    plt.legend()
    plt.show()
