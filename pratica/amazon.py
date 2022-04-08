import requests
from bs4 import BeautifulSoup
import pandas as pd

#Itens mais vendidos em Eletrônicos NA AMAZON e seus preços.

lista = []

response = requests.get('https://www.amazon.com.br/gp/bestsellers/electronics')

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'zg-grid-general-faceout'})

for produto in produtos:
    tituloDoProduto = produto.find('div', attrs={'class': '_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-3__g3dy1'})
    if tituloDoProduto:
        precoDoProduto = produto.find('span', attrs={'class': 'p13n-sc-price'})

        print(tituloDoProduto.text)
        if precoDoProduto:
            print(precoDoProduto.text)

    else:
        tituloDoProduto = produto.find('div', attrs={'class': '_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-4__2q2cc'})
        precoDoProduto = produto.find('span', attrs={'class': 'p13n-sc-price'})

        print(tituloDoProduto.text)
        if precoDoProduto:
            print(precoDoProduto.text)
    
    print('\n')
    if precoDoProduto:
        lista.append([tituloDoProduto.text, precoDoProduto.text])
    else:
        lista.append([tituloDoProduto.text, 'None'])

tabela = pd.DataFrame(lista, columns=['Titudo do produto', 'Preço do produto'])
tabela.to_excel('excel.xlsx', index=False)