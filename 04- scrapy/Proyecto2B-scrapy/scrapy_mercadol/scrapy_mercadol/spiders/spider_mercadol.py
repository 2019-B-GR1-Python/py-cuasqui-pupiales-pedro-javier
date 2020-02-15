
#arania_fybeca.py
import scrapy
from scrapy_mercadol.items import ProductoMercadol
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class AraniaMercadol (CrawlSpider):
  name="mercadol"
  allowed_domains=[##heredado override
  'listado.mercadolibre.com.ec']
  global categoria 
  start_urls= [#Herresado override
    'http://home.mercadolibre.com.ec/vehiculos-accesorios/',
    'http://home.mercadolibre.com.ec/alimentos-bebidas/',
    'http://home.mercadolibre.com.ec/animales-y-mascotas/',
    'https://home.mercadolibre.com.ec/arte-antiguedades/',
    'https://www.mercadolibre.com.ec/vehiculos/',
    'http://home.mercadolibre.com.ec/bebes/',
    'http://home.mercadolibre.com.ec/belleza-cuidado-personal/',
    'http://home.mercadolibre.com.ec/fotografia/',
    'http://home.mercadolibre.com.ec/telefonia-y-celulares/',
    'http://home.mercadolibre.com.ec/coleccionables/',
    'http://home.mercadolibre.com.ec/computacion/',
    'http://home.mercadolibre.com.ec/video-juegos/',
    'http://home.mercadolibre.com.ec/deportes-y-fitness/',
    'http://home.mercadolibre.com.ec/electronica/',
    'http://home.mercadolibre.com.ec/hogar-y-muebles/',
    'http://home.mercadolibre.com.ec/industrias-oficinas/',
    'https://www.mercadolibre.com.ec/inmuebles/',
    'http://home.mercadolibre.com.ec/instrumentos-musicales/',
    'http://home.mercadolibre.com.ec/joyas-relojes/',
    'http://home.mercadolibre.com.ec/juegos-y-juguetes/',
    'http://home.mercadolibre.com.ec/musica-libros-y-peliculas/',
    'http://home.mercadolibre.com.ec/recuerdos-cotillon-fiestas/',
    'http://home.mercadolibre.com.ec/ropa-accesorios/',
    'http://home.mercadolibre.com.ec/salud-equipamiento-medico/',
    'http://www.mercadolibre.com.ec/servicios/',
    'http://home.mercadolibre.com.ec/otras-categorias/'

  ]
  regla_uno = ( #Busca todo
    Rule (
      LinkExtractor(),callback='parse_page'
      ),  
  )

  rules = regla_uno #Heredado override  
  #página de fybeca, categoria de vitaminas
  # urls =[
  #   'https://listado.mercadolibre.com.ec/acc-motos-cuatrimotos/'
  # ]


  def start_requests(self):
    for url in self.start_urls:
      yield scrapy.Request(url=url)

  def parse_page (self, response):
    productos = response.css('li.results-item')
    categoria = response.css('aside.filters.stack .breadcrumb ol :first-child span::text').extract_first()

    for producto in productos:
      # Los ITEMS proporcionan el contenedor de datos SCRAPEADOS, mientras que los cargadores de ITEMS proporcionan el mecanismo para llenar ese contenedor.
      if(len(categoria)>0):
        producto_loader= ItemLoader(item = ProductoMercadol(),selector=producto )
        # Todas las propiedades de la clase van a tener por defecto el defaul_output_procesor
        producto_loader.default_output_processor = TakeFirst()
        #Pasa el nombre d ela propiedad que pasamos en el item, y el selector div.product-tile-inner
        producto_loader.add_value('categoria',categoria)
        producto_loader.add_css('titulo', 'div.item__info-container h2.item__title a .main-title::text')
        producto_loader.add_xpath('ruta_detalles','div[contains(@class,"rowItem")]/div[contains(@class, "item__image")]/div[contains(@class, "images-viewer")]/div[contains(@class, "image-content")]/a[contains(@class,"figure")]/@href') #img/@src
        #si no contiene imagen, el arreglo contiene null
        producto_loader.add_css('precio_fraccion','div.item__info-container span.price__fraction::text')
        
        if(len(producto.css('div.item__info-container span.price__decimals::text').extract())>0 ):
          print("EXISTE OBJETO #################################################3")
          #no todos los elementos contienen precio en decimales
          producto_loader.add_css('precio_decimales','div.item__info-container span.price__decimals::text')
        else:
          print("NO EXISTE OBJETO ************************************************")
          producto_loader.add_value('precio_decimales',0)
          
        producto_loader.add_css('provincia','div.item__info-container div.item__condition::text')
  # con los items se puede hacer validaciones(es más complicado)
        yield producto_loader.load_item()