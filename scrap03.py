import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# a class = 'feed-post-link gui-color-primary gui-color-hover'

# Título
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

# x.text Mostra o texto de dentro da div
print(titulo.text)


# Subtítulo
subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})

print(subtitulo.text)