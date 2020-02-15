
#arania_fybeca.py
import scrapy
from arania_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst



class AraniaFybeca (scrapy.Spider):
  name="fybeca"
  #página de fybeca, categoria de vitaminas
  urls =[
    'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25'
  ]


  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url)

  def parse (self, response):
    productos = response.css('div.product-tile-inner')

    for producto in productos:
      detalle = producto.css('div.detail')
      tiene_detalle= len(detalle) >0
      if(tiene_detalle):
        # Los ITEMS proporcionan el contenedor de datos SCRAPEADOS, mientras que los cargadores de ITEMS proporcionan el mecanismo para llenar ese contenedor.
        producto_loader= ItemLoader(item = ProductoFybeca(),selector=producto )
        # Todas las propiedades de la clase van a tener por defecto el defaul_output_procesor
        producto_loader.default_output_processor = TakeFirst()
        #Pasa el nombre d ela propiedad que pasamos en el item, y el selector div.product-tile-inner
        producto_loader.add_css('titulo', 'a.name::text')
        producto_loader.add_xpath('imagen',                     'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
  # con los items se puede hacer validaciones(es más complicado)
        yield producto_loader.load_item()