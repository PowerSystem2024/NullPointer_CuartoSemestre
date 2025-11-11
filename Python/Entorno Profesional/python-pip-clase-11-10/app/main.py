import utils
import read_csv
import charts
import pandas as pd
def run():
  df=pd.read_csv('./data.csv')#Estamos leyendo el archivo csv con pandas
  df= df[df['Continent']=='South America']#Filtramos los datos por continente
  countries = df['Country'].values#Obtenemos los paises
  percentages = df['World Population Percentage']#Obtenemos los porcentajes de pobl
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('./data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()