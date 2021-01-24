import requests

import re

from bs4 import BeautifulSoup

import threading


DOMINIO = 'https://django-anuncios.solyd.com.br'

URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'

TELEFONES = []


def buscar(url):
	try:
		resposta = requests.get(url)
		return resposta.text
	except:
		print('Houve algum erro!')
		
def parsing(resposta_url):
	try:
		soup = BeautifulSoup(resposta_url, 'html.parser')
		return soup
	except:
		print('Ocorreu alum problema!')
		
def buscar_anuncio(soup):
	cards_pai = soup.find('div', class_='ui three doubling link cards')
	cards = cards_pai.find_all('a')
	links = []
	for card in cards:
		link = card['href']
		links.append(link)

		
	return links
	
def encontrar_anuncios(soup):
	try:
		anuncio = soup.find_all('div', class_='sixteen wide column')[2].p.get_text().strip()
		print('Anuncios:',anuncio,'\n')
	except:
		print('Houve algum problema!')
	
	
def mostrar_anuncios():
	num = 0
	for num in range(1,14):
		resposta = buscar(URL_AUTOMOVEIS)
		soup = parsing(resposta)
		resposta = buscar_anuncio(soup)
		anuncio = buscar(DOMINIO + resposta[num])
		soup_anuncio = parsing(anuncio)
		encontrar_anuncios(soup_anuncio)
	
	
def encontrar_telefones(soup):
	try:
		anuncio = soup.find_all('div', class_='sixteen wide column')[2].p.get_text().strip()
	except:
		print('Houve algum problema!')			
	regex = re.findall(r"\(?0?([1-9]{2})[ \-\.]{0,2}(9\d{4})[ \-\.]?(\d{4})", anuncio)
	print('Possiveis números de telefone: ', regex)
	

def mostrar_telefones():
	num = 0
	for num in range(1,14):
		resposta = buscar(URL_AUTOMOVEIS)
		soup = parsing(resposta)
		resposta = buscar_anuncio(soup)
		anuncio = buscar(DOMINIO + resposta[num])
		soup_anuncio = parsing(anuncio)
		encontrar_telefones(soup_anuncio)
	


#mostrar_anuncios()

mostrar_telefones()


	





