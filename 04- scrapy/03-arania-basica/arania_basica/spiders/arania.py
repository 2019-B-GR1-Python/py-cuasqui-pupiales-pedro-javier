#################################33
######CRAWLING ###################3
###################################33
import scrapy
import pandas as pd
class IntroSpider(scrapy.Spider):
  #name: @overide, debe ser siempre name
  name = 'introduccion_spider'# !!!importante ,este nombre permite identificar a la clase
  # urls=['http://books.toscrape.com/catalogue/category/books/travel_2/index.html'];
  urls=['http://books.toscrape.com/catalogue/category/books/travel_2/index.html', 
  'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
  'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
  'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
  'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
  'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
  'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
  'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
  'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
  'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
  'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
  'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
  'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
  'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
  'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
  'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
  'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
  'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
  'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
  'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
  'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
  'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
  'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
  'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
  'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
  'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
  'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
  'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
  'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
  'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
  'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
  'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
  'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
  'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
  'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
  'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
  'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
  'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
  'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
  'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
  'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
  'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
  'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
  'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
  'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
  'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
  'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
  'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
  'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
  'http://books.toscrape.com/catalogue/category/books/crime_51/index.html ',] ;


#start_request: @overrideJ
  #ejecuta la peticion a la URL y descarga el documento
  def start_requests(self):# enviar la referencia a la instancia de la clase con self
    #aqui se hacen todas las peticiones del scrapy 
      for url in self.urls:
        #yield permite esperar hasta que se complete la línea, 
        yield scrapy.Request(url=url)
  
  #parse: @overide
  #Toma la respuesta de la funcion start_requests() y la permite su procesamiento
  def parse(self, response):
      genero= response.css('title::text').extract_first();
      print(f"######################## {genero} ####################################");
      etiqueta_contenedora = response.css('article.product_pod');
      titulos = etiqueta_contenedora.css('h3 > a::text').extract() #se pueden concatenar las variables de tipo response.css
      precios = etiqueta_contenedora.css('div.product_price> p.price_color::text').extract()
      url_images = etiqueta_contenedora.css('div.image_container a img::attr(src)')

      self.insertar_libro(titulos,precios, url_images,genero)
      # print(titulos);
      # print(precios)
      # print(url_images)
  def insertar_libro(self, titulos, precios, url_images,genero):

      libros= pd.DataFrame(titulos)
      libros["precios"]=precios
      libros["url_images"]=url_images
      try:
        path="./libros.txt"
        archivo_abierto=open(path,mode="a")
        contador=0
        for titulo in titulos:
          archivo_abierto.write("********************************"+genero+'**************************\n')
          archivo_abierto.write(titulo +" | "+ precios[contador]+" | "+ url_images[contador]+ "\n")
          contador= contador + 1
          # archivo_abierto.write(libro + "\n")
        archivo_abierto.close
      except Exception as error:
        print(f"error {error}")

      ##tarea: Sacar url de imagenes, precio en flotante y el titulo de la página travel
      ##tarea: SAcar los mismos datos para toda la lista de enlaces al nivel de travel
      ##tarea: Guardar todos los datos en un archivo
      # http://books.toscra
      # pe.com/catalogue/category/books/travel_2/index.html