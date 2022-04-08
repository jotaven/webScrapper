import requests
from bs4 import BeautifulSoup
import pandas as pd #cria tabelas para o python

lista_noticias = []

response = requests.get('https://g1.globo.com')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    # a class = 'feed-post-link gui-color-primary gui-color-hover'

    # Título
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    # x.text Mostra o texto de dentro da div
    #print('\n', titulo.text)
    #print(titulo['href']) # pegar o link da noticia

    # Subtítulo
    subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})

    if subtitulo:
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False) #index=False remover a numeração 0-999... de colunas

#print(news)