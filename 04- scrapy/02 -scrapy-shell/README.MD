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

14-01-2020

### Seleccionar usando xpath

```
Para copiar el cpath del codigo html, clic derecho en la etiqueta dentro del inspector de codigo -> seleccionar copy -> seleccionar xpath
```

```
La propiedad xpath permite seleccionar elementos html por medio de su xpath
```

In [3]: response.xpath('/html/head/title').extract()
Out[3]: ['<title>Quotes to Scrape</title>']

```
Doble slash antes del title indica que debe seleccionar todas las etiquetas que tengan xpath title
```

In [4]: response.xpath('//title').extract()  
Out[4]: ['<title>Quotes to Scrape</title>']

In [5]: response.xpath('/html/body/div/div[2]/div[2]/h2').extract()  
Out[5]: ['<h2>Top Ten tags</h2>']

```
/text() al final del string xpath obtiene el texto del elemento o elementos seleccionados
```

In [6]: response.xpath('/html/body/div/div[2]/div[2]/h2/text()').extract()  
Out[6]: ['Top Ten tags']

```
Se puede seleccionar las clases de un elemento usando [@class='clase']
```

In [7]: response.xpath("//div[@class='quote']").extract()

In [8]: response.xpath("//div[@class='quote']/span[@class='text']").extract()

In [9]: response.xpath("//div[@class='quote']/span[@class='text']").extract()  
Out[9]:  
['<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>',
'<span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>',
'<span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>',
'<span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>',
'<span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it\'s better to be absolutely ridiculous than absolutely boring.”</span>',
'<span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>',
'<span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>',
'<span class="text" itemprop="text">“I have not failed. I\'ve just found 10,000 ways that won\'t work.”</span>',
'<span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it\'s in hot water.”</span>',
'<span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>']

```
Extrae el primer elemento de toda la lista
```

In [10]: response.xpath("//div[@class='quote']/span[@class='text']").extract_first()  
Out[10]: '<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>'

```
Obtener el link con xpath
```

In [11]: response.xpath("//div[@class='quote']/span/a[@href]").extract()  
Out[11]:  
['<a href="/author/Albert-Einstein">(about)</a>',
'<a href="/author/J-K-Rowling">(about)</a>',
'<a href="/author/Albert-Einstein">(about)</a>',
'<a href="/author/Jane-Austen">(about)</a>',
'<a href="/author/Marilyn-Monroe">(about)</a>',
'<a href="/author/Albert-Einstein">(about)</a>',
'<a href="/author/Andre-Gide">(about)</a>',
'<a href="/author/Thomas-A-Edison">(about)</a>',
'<a href="/author/Eleanor-Roosevelt">(about)</a>',
'<a href="/author/Steve-Martin">(about)</a>']  
In [12]: response.xpath("//div[@class='quote']/span/a/@href").extract()  
Out[12]:  
 ['/author/Albert-Einstein',
 '/author/J-K-Rowling',
 '/author/Albert-Einstein',
 '/author/Jane-Austen',
 '/author/Marilyn-Monroe',
 '/author/Albert-Einstein',
 '/author/Andre-Gide',
 '/author/Thomas-A-Edison',
 '/author/Eleanor-Roosevelt',
 '/author/Steve-Martin']
