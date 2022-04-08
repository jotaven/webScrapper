'''Selenium: web driver/controlar o navegador'''
#1. baixar o driver do navegador e deixar na mesma pasta do arquivo .py

#2. importar selenium webdriver.
from selenium import webdriver

from time import sleep

#3. Atribuir o driver a uma variavel.
#       webdriver → Chrome → executable_path=r'./chromedriver.exe'
navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

navegador.get('https://www.walissonsilva.com/blog')

#dar um tempinho pra mostrar o que está ocorrendo
sleep(3)

#encontra o elemento pela tag ('x')

elemento = navegador.find_element_by_tag_name('input')

#Escreve no elemento que você pediu para encontrar
elemento.send_keys('data')