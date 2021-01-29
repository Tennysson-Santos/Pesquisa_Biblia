import requests

import re

from bs4 import BeautifulSoup


BIBLIA = []

def buscar_url(url):
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
		print('Ocorreu algum problema!')
		
def buscar_livro(soup):
	try:
		livro = soup.find('div', class_='jss40')
		versiculos = len(livro.find_all('p'))
		print(f'Este capítulo tem: {versiculos - 1} versículos!')
		num = int(input('\nEscolha um versículo: '))
		num -= 1
		livros = livro.find_all('p')[num].get_text().strip()
		return livros
	except:
		print('Ocorreu algum problema!')

def mostrar_livro():
	try:
		busca = buscar_url(URL)
		soup = parsing(busca)
		livro = buscar_livro(soup)
		print(livro)	
	except Exception as error:
		print('Ocorreu algum problema')
		print(error)
	
def capitulo():
	resposta = buscar_url('https://www.bibliaonline.com.br/naa/'+livro)
 
	parsi = parsing(resposta)

	capitulo = len(parsi.find('ul', class_='jss1'))

	print(f'Este livro tem {capitulo} capítulos!')
	
def salvar_livro():
	busca = buscar_url(URL)
	soup = parsing(busca)
	livro = buscar_livro(soup)
	BIBLIA.append(livro)
	print(livro)
	with open('biblia.doc', 'w') as arquivo:
		arquivo.write(f'{BIBLIA}')

if __name__ == "__main__":
	print('-----------------------------')
	print('      LEIA A BÍBLIA!'          )
	print('-----------------------------')
	print('Escolha um livro da bíblia, Ex Matheus[mt]')


livro = input('\nDigite um livro: ')
capitulo()
cap = int(input('\nEscolha um capítulo: '))
URL = 'https://www.bibliaonline.com.br/naa/'+livro+'/'+str(cap)
#salvar_livro()
mostrar_livro()

