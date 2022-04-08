from bs4 import BeautifulSoup
import requests

response = requests.get('https://g1.globo.com/pb/paraiba/cidade/joao-pessoa/')

site = BeautifulSoup(response.text, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    print(titulo.text)
    if subtitulo:
        print(subtitulo.text)
    print('\n\n')