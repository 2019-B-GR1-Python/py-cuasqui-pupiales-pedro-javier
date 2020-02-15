# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto):
    url_fybeca = 'https://www.fybeca.com'
    # la cadena de texto que vaa ser reemplazada
    cadena_texto = '../..'
    return texto.replace(cadena_texto, url_fybeca)
# se cere el item par aque se instancie en cada página
class ProductoFybeca(scrapy.Item):
    # se puede setear con imputs y outputss processors
    titulo= scrapy.Field( ) # se pueden agregar los campos 
# Esta clase se va a crear en cada instancia de scrapy
    imagen = scrapy.Field(
          #agregar el numero de funciones que deseamos ejecutar
        # llenar en el loader la arania
        input_processor= MapCompose( transformar_url_imagen),
        output_processor = TakeFirst()
    )

class AraniaFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
