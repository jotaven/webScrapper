
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

from attr import attr
import requests
from bs4 import BeautifulSoup
import pandas as pd

numProdutos = 1

lista_produtos = []

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated'})


if produtos:
    for produto in produtos:
        titulo = produto.find('h2', attrs={'class': 'ui-search-item__title ui-search-item__group__element'})

        link = produto.find('a', attrs={'class': 'ui-search-result__content ui-search-link'})

        cifra = produto.find('span', attrs={'class': 'price-tag-symbol'})
        real = produto.find('span', attrs={'class': 'price-tag-fraction'})
        centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

        #print(produto.prettify(), '\n')
        #print(f'{numProdutos}.')
        #numProdutos += 1
        #print('Titulo do produto: ', titulo.text)
        #print('Link do produto: ', link['href'])
        if centavos: # se centavos for diferente de vazio (none)
            #print(f'Preço do produto: {cifra.text} {real.text},{centavos.text}')
            lista_produtos.append([titulo.text, (cifra.text + real.text + ',' + centavos.text), link['href']])
        else:
            ##print(f'Preço do produto: {cifra.text} {real.text},00')
            lista_produtos.append([titulo.text, (cifra.text + real.text + ',00'), link['href']])
        #print('\n\n')
else:
    produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
    for produto in produtos:
        titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

        link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})

        cifra = produto.find('span', attrs={'class': 'price-tag-symbol'})
        real = produto.find('span', attrs={'class': 'price-tag-fraction'})
        centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

        #print(produto.prettify(), '\n')
        #print(f'{numProdutos}.')
        #numProdutos += 1
        #print('Titulo do produto: ', titulo.text)
        #print('Link do produto: ', link['href'])
        if centavos: # se centavos for diferente de vazio (none)
            #print(f'Preço do produto: {cifra.text} {real.text},{centavos.text}')
            lista_produtos.append([titulo.text, (cifra.text + real.text + ',' + centavos.text), link['href']])
        else:
            #print(f'Preço do produto: {cifra.text} {real.text},00')
            lista_produtos.append([titulo.text, (cifra.text + real.text + ',00'), link['href']])
        #print('\n\n')


news = pd.DataFrame(lista_produtos, columns=['Titulo', 'Preço', 'Link'])
news.to_excel('produtos.xlsx', index=False)