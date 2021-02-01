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
	print('\t                    ----------------------')
	print(' \t                        LEIA A BÍBLIA!'          )
	print('\t                    ----------------------')
	print('\t                 Escolha um livro da bíblia!!\n')
	print('''\t              *----* Velho Testamento *----*\n
Gênesis[gn] - Êxodo[ex] - Levítico [lv] - Números[nm] - Deuteronômio[dt]\n
Josué[js] - Juízes[jz] - Rute[rt] - 1 Samuel[1sm] - 2 Samuel[2sm] - 1 Reis[1rs]\n
2 Reis[2rs] - 1 Crônicas[1cr] - 2 Crônicas[2cr] - Esdras[ed] - Neemias[ne]\n 
Ester[et] - Jó[jó] - Salmos[sl] - Provérbios[pv] - Eclesiastes[ec]\n
Cânticos[ct] - Isaías[is] - Jeremias[jr] - Lamentações[lm] - Ezequiel[ez]\n
Daniel[dn] - Oséias[os] - Joel[jl] - Amós[am] - Obadias[ob] - Jonas[jn]\n
Miquéias[mq] - Naum[na] - Habacuque[hc] - Sofonias[sf] - Ageu[ag] - Zacarias[zc] - Malaquias[ml]\n
''')
	print('''\t              *----* Novo Testamento *----\n*
Mateus[mt] - Marcos[mc] - Lucas[lc] - João[jo] - Atos[atos] - Romanos[rm]\n
1 Coríntios[1co] - 2 Coríntios[2co] - Gálatas[gl] - Efésios[ef] - Filipenses[fp]\n
Colossenses[cl] - 1 Tessalonicenses[1ts] - 2 Tessalonicenses[2ts] - 1 Timóteo[1tm]\n
2 Timóteo[2tm] - Tito[tt] - Filemom[fm] - Hebreus[hb] - Tiago[tg] - 1 Pedro[1pe]\n
2 Pedro[2pe] - 1 João[1jo] - 2 João[2jo] - 3 João[3jo] - Judas[jd] - Apocalipse[ap]\n
''')

livro = input('\nDigite um livro: ')
capitulo()
cap = int(input('\nEscolha um capítulo: '))
URL = 'https://www.bibliaonline.com.br/naa/'+livro+'/'+str(cap)
#salvar_livro()
mostrar_livro()

