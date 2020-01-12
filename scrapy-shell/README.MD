#SCRAPY
#instalcion de scrapy

```
$pip install scrapy
```

```
Ver caracteristicas de rendimiento de scrapy
```

```
$scrapy bench
```

```
Consultar la configuracion de scrappy
```

```
$scrapy settings
```

```
Consultar la version de scrappy
```

```
$scrapy version
```

### scrapy view `url`

Ejemplo con la página web del SRI

```
>scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```

### scrapy shell `url`

permite interactuar con la respuesa de scrapy -> se abre un interpretador de python que tiene cargada la página de la URL

```
>scrapy shell http://quotes.toscrape.com/
```

Una vez que se abre el shell, se pueden ejecutar los comandos en python

In [1]: tupla = (4,5,6)  
In [2]: tupla  
Out[2]: (4, 5, 6)  
In [3]: print ('hola')  
hola

In [4]: response.css('title')  
Out[4]: [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

In [5]: response.css('title').extract()  
Out[5]: ['<title>Quotes to Scrape</title>']

In [6]: response.css('title::text').extract()  
Out[6]: ['Quotes to Scrape']

In [7]: response.css('.author::text').extract()  
Out[7]:

In [8]: type(response.css('.author::text'))  
Out[8]: scrapy.selector.unified.SelectorList

lOS TRES SIGUIENTES COMANDOS FUNCIONAN IGUAL

<!--  -->

In [13]: response.css('.author::text')[0].extract()  
Out[13]: 'Albert Einstein'

In [14]: response.css('.author::text').extract()[0]  
Out[14]: 'Albert Einstein'

In [15]: response.css('.author::text').extract_first()  
Out[15]: 'Albert Einstein'

<!--  -->

ANEXOS, PROMPT COMPLETO

<!--



 -->
