import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--headless') #não abrir a pagina para o usuário ver;
# definir o tamanho da pagina (px,px)
options.add_argument('window-size=1240,1050')
options.add_experimental_option("detach", True)  # deixar a janela aberta

navegador = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe', options=options)

navegador.get('https://airbnb.com')

sleep(2)

input_place = navegador.find_element_by_xpath('//*[@id="bigsearch-query-location-input"]')
input_place.send_keys('João Pessoa')
input_place.submit()

sleep(0.8)

button_ar_condicionado = navegador.find_element_by_xpath('//*[@id="menuItemButton-toggleItem-dynamic_amenities-Ar-condicionado-Ar-condicionado"]/button')
button_ar_condicionado.click()

button_mar = navegador.find_element_by_xpath('//*[@id="menuItemButton-toggleItem-dynamic_amenities-Em frente ao mar-Em frente ao mar"]/button')
button_mar.click()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

