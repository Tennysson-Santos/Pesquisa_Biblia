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
		print('Ocorreu alum problema!')
		
def buscar_livro(soup):
	try:
		livro = soup.find('div', class_='jss40')
		num = int(input('\nDigite o versículo: '))
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
	print('Consulta de livros da Biblia!')
	print('-----------------------------')
	print('Escolha um livro da biblia, Ex Matheus[mt]')
	print('Escolha um Capitulo do livro, Ex [1]')

livro = input('\nDigite um livro: ')
cap = int(input('\nDigite um capítulo: '))
URL = 'https://www.bibliaonline.com.br/naa/'+livro+'/'+str(cap)
salvar_livro()
#mostrar_livro()


