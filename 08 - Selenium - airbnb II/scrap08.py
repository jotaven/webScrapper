import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
#options.add_argument('--headless') #não abrir a pagina para o usuário ver;

options.add_argument('window-size=1240,1050') # definir o tamanho da pagina (px,px)
#options.add_experimental_option("detach", True)  # deixar a janela aberta

navegador = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe', options=options)

navegador.get('https://airbnb.com.br')

sleep(2)

input_place = navegador.find_element_by_xpath('//*[@id="bigsearch-query-location-input"]')
input_place.send_keys('João Pessoa')
input_place.submit()

sleep(3)

closeTraduction = navegador.find_element_by_xpath('/html/body/div[11]/div/div/div/div[3]/button')
closeTraduction.click()

filterButton = navegador.find_element_by_xpath('//*[@id="filter-menu-chip-group"]/div[2]/div/div[4]/button')
filterButton.click()
sleep(1)
checkbox_mar = navegador.find_element_by_xpath('//*[@id="filterItem--checkbox-kg_and_tags-Tag:789-row-checkbox"]')
checkbox_mar.click()
checkbox_ar_condicionado = navegador.find_element_by_xpath('//*[@id="filterItem--checkbox-amenities-5-row-checkbox"]')
checkbox_ar_condicionado.click()
sleep(1)

#Clicar em um butão de tag <a href=''></a>
navegador.find_element_by_link_text('Mostrar mais de 300 acomodações').click()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

dados_hospedagens = []


hospedagens = site.findAll('div', attrs={'itemprop': 'itemListElement'})
#print(hospedagem.prettify())

for hospedagem in hospedagens:
    hospedagem_descricao = hospedagem.find('meta', attrs={'itemprop': 'name'})
    hospedagem_descricao = hospedagem_descricao['content']

    hospedagem_link = hospedagem.find('meta', attrs={'itemprop': 'url'})
    hospedagem_link = hospedagem_link['content']

    print('Descrição:', hospedagem_descricao)
    print('Url:', hospedagem_link)

    hospedagem_detalhes = hospedagem.find('div', attrs={'style': '--margin-bottom:var(--h-x-sf-jw);'}).text
    print('Detalhes:', hospedagem_detalhes)

    preco = hospedagem.findAll('span')[-1].text #procura TODOS as tags 'span' e procura apenas o ultimo [-1]
    print('Preço da hospedagem:', preco)
    print('\n')
    
    dados_hospedagens.append([hospedagem_descricao, hospedagem_link, hospedagem_detalhes, preco])

dados = pd.DataFrame(dados_hospedagens, columns=['Descrição', 'Url', 'Detalhes', 'Preço'])
dados.to_excel('hospedagens.xlsx', index=False)
