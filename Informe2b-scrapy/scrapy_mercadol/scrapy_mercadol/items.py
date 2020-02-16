# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


class ProductoMercadol(scrapy.Item):
    # se puede setear con imputs y outputss processors
    categoria = scrapy.Field()
    titulo= scrapy.Field( ) # se pueden agregar los campos 
# Esta clase se va a crear en cada instancia de scrapy
    ruta_detalles = scrapy.Field( )
    precio_fraccion= scrapy.Field()
    precio_decimales= scrapy.Field()
    provincia= scrapy.Field()

class ScrapyMercadolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
