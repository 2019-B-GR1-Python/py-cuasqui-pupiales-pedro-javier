#################################33
######CRAWLING ###################3
###################################33
import scrapy
class IntroSpider(scrapy.Spider):
  #name: @overide, debe ser siempre name
  name = 'introduccion_spider'# !!!importante ,este nombre permite identificar a la clase
  # urls=['http://books.toscrape.com/catalogue/category/books/travel_2/index.html'];
  urls=['http://books.toscrape.com/catalogue/category/books/travel_2/index.html', 
  'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',] ;


#start_request: @override
  #ejecuta la peticion a la URL y descarga el documento
  def start_requests(self):# enviar la referencia a la instancia de la clase con self
    #aqui se hacen todas las peticiones del scrapy 
      for url in self.urls:
        #yield permite esperar hasta que se complete la línea, 
        yield scrapy.Request(url=url)
  
  #parse: @overide
  #Toma la respuesta de la funcion start_requests() y la permite su procesamiento
  def parse(self, response):
      etiqueta_contenedora = response.css('article.product_pod');
      titulos = etiqueta_contenedora.css('h3 > a::text').extract() #se pueden concatenar las variables de tipo response.css
      precios = etiqueta_contenedora.css('div.product_price> p.price_color::text').extract()

      url_images = etiqueta_contenedora.css('div.image_container a img::attr(src)')

      print(titulos);
      print(precios)
      print(url_images)



      ##tarea: Sacar url de imagenes, precio en flotante y el titulo de la página travel
      ##tarea: SAcar los mismos datos para toda la lista de enlaces al nivel de travel
      ##tarea: Guardar todos los datos en un archivo
      http://books.toscrape.com/catalogue/category/books/travel_2/index.html