# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class SoloCarrosPipeline(object):
    def process_item(self, item, spider):
        # se carga desde el ItemLoader de ANARIA_FYBECA.PY
        categoria = item['categoria']
        titulo= item['titulo']
        ruta_detalles= item['ruta_detalles'] 
        precio_fraccion= item['precio_fraccion']
        precio_decimales= item['precio_decimales']
        provincia= item['provincia']
        if(ruta_detalles == ''):
        #raise es como throw error
            raise DropItem('No contiene detalles')
        else:
            return item

class ScrapyMercadolPipeline(object):
    def process_item(self, item, spider):
        return item
