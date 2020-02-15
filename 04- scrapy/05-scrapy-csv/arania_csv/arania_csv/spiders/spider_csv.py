from scrapy.spiders import CSVFeedSpider

class VinosBlancosArania(CSVFeedSpider):
  # Se define el nombre de la arania
  name ="vinos"
# Define la url base
  start_urls =[
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
  ]
  
  # OPCIONES PARA EL ARCHIVO CSV
# delimitador para cada registro
  delimiter=";"
  # caracter para los strings
  quotechar:'"'
  # Selecciona TODAS LAS COLUMNAS
  headers = [
        'fixed density',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
        'quality'
    ]

# Self, response, row(nuevo):
def parse_row(self, response, row):
  print(type(row))
  # print('ph=', row['PH'] )
  # print('citric acid = ', row['citric acid'])
  with open('archivo.txt','a+', encoding='utf-8') as archivo:
    archivo.write(row['pH'] + '\n')
