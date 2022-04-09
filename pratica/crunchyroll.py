from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import pandas as pd

options = Options()
options.add_argument('window-size=1240,1050')
options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(
    executable_path=r'C:\WebDrivers\chromedriver.exe', options=options)
navegador.get('https://www.crunchyroll.com/pt-br/videos/anime')
sleep(2)
navegador.find_element_by_xpath('//body').send_keys(Keys.END) #Rola até o fim da pagina
sleep(1)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

dados_animes = []

animes = site.findAll('div', attrs={
                      'class': 'wrapper hover-toggle-queue container-shadow hover-classes'})
for anime in animes:
    anime_titulo = anime.find(
        'span', attrs={'class': 'series-title block ellipsis'}).text
    anime_eps = anime.find(
        'span', attrs={'class': 'series-data block ellipsis'}).text.strip()
    print('titulo:', anime_titulo)
    print('Episodios:', anime_eps)
    dados_animes.append([anime_titulo, anime_eps])
    print('')

print(datetime.today().strftime('%d-%m-%Y %H:%M'))

dados = pd.DataFrame(dados_animes, columns=['Titulo', 'Episodios Totais'])
dados.to_excel('popularAnimes.xlsx', index=False)
