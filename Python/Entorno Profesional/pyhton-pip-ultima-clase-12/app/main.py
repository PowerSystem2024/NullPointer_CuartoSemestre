import utils
import read_csv
import charts
import pandas as pd

# Función principal para ejecutar el programa
def run():
  '''   # leemos el csv, gracias al módulo línea 2
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)'''

  data = read_csv.read_csv('./data.csv')
  df=pd.read_csv('./data.csv')
  df= df[df['Continent']=='South America']
  countries = df['Country'].values
  percentages = df['World Population Percentage']


  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels=labels, values=values, name=country['Country'])

# Ejecutar la función principal si el archivo es ejecutado directamente
if __name__ == '__main__':
  run()