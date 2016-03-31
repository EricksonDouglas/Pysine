#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pysine.py
#  
#  Copyright 2016 Erickson <erickshowplay@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time,argparse,os
from urllib.request import urlopen
try:
	from bs4            import BeautifulSoup
except ImportError:
	print(Colorir.YELLOW+'''
BeautifulSoup4 não instalado
Faça a instalação do BeautifulSoup
[+] pip install -r requisitos.txt
'''+Colorir.ENDC)
	exit(1)	



#Colorir o shell
######################################################################
class Colorir:
	OKGREEN = '\033[92m'
	GREEN = "\033[1;32m"
	GREENUNDER	=	"\033[4;32m"
	RED = '\033[91m'
	WARNING = '\033[93m'
	BASICY = "\033[0;33m"
	YELLOW = "\033[1;33m"
	BRED = "\033[0;31m"
	RED2 = "\033[1;31m"
	UNDERLINE = '\033[4m'
	ENDC = '\033[0m'

#mensagens das variavel
######################################################################
class Mensagem:
	author   = """

[+]	Author:   Erickson Douglas  
[+]	Facebook: erickshow.mattos
[+]	Twitter:  @erickshowplay 

"""
	exemplos = Colorir.GREEN+"""
	Exemplos

[+] Modo Interativo
"""+Colorir.BRED+"""./pysine -i
"""+Colorir.GREEN+"""[+] Mostrando o resultado do emprego Estagiario na Cidade Crato/PE
"""+Colorir.BRED+"""python3 pysine -e Estagiario --cidades Crato/CE

"""+Colorir.GREEN+"""[+] Mostrando os ultimos resultado da Cidade Crato/PE e das Cidades próximos 
"""+Colorir.BRED+"""python3 pysine --cidades Crato/CE 

"""+Colorir.GREEN+"""[+] Salvando o resultado dos empregos da cidade Juazeiro do norte no arquivo vendedor.txt 
"""+Colorir.BRED+"""./pysine -c juazeiro-do-norte/ce --empregos Vendedor,vendedor-externo --salvar vendedor.txt

"""+Colorir.GREEN+"""[+] Criando e Salvando resultado dos empregos nas Cidades Fortaleza/CE e Recife/pe no arquivo programador.txt dentro da pasta empregos 
"""+Colorir.BRED+"""python3 pysine -c FORTALEZA/CE,recife/pe -e web-programador,desenvolvedor,analista-desenvolvimento-de-sistemas -s ~/empregos/programador.txt"""+Colorir.ENDC
	
	errorAcento = Colorir.WARNING+"""
[-]Erro no argumento
[-]-------------------------------------------------------
[-]não precisa colocar acento no nome da Cidade e/ou Emprego
[-]Tente novamente!
__________________________________________________________"""+Colorir.ENDC

	errorArgumento =Colorir.WARNING+"""
[-]Esqueceu de algum argumento!
[-]-----------------------------
[-]Tente novamente"""+Colorir.ENDC

	resultado="""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

{Empresadt} : {Empresadd}
{Salariodt} : {Salariodd}
{Cidadedt}  : {Cidadedd}
{Descricdt} : {Descricdd}

Link : {url}
"""
	
	errorBeautifulSoup = Colorir.YELLOW+'''
____________________________________
BeautifulSoup4 não instalado
Faça a instalação do BeautifulSoup
[+] pip install -r requisitos.txt

'''+Colorir.ENDC

	errorEstado = Colorir.YELLOW+"\nEsqueceu colocar o Estado, exemplos:Bodoco/pe, juazeiro-do-norte/CE\nTente novamente "+Colorir.ENDC
	
	Cancelado   = Colorir.YELLOW+"\nCancelado com Sucesso\n"+Colorir.ENDC
	
	Novamente   = Colorir.YELLOW+"\nTente novamente\n"+Colorir.ENDC
	EmpregoNot  = Colorir.WARNING+"""
[-]
[-] Emprego não encontrado:
[-]
Link :"""+Colorir.GREEN+""" {url}"""

#pegando as informação de cada link
######################################################################
def mostraremprego(complemento_link,salvar):
	dt,dd = list(),list()
	link  = "http://www.sine.com.br{complemento}".format(complemento=complemento_link)
	try:
		soup = BeautifulSoup(urlopen(link),"html.parser")
	except ConnectionResetError:
		time.sleep(5)
		soup = BeautifulSoup(urlopen(link),"html.parser")
		print("Tentando conectar novamente!")
		
	for row in soup.find("dl",{"class":"dl-horizontal"}).find_all("dt"):
		dt.append(row.get_text().rstrip().strip())
		
	for row in soup.find("dl",{"class":"dl-horizontal"}).find_all("dd"):
		dd.append(row.get_text().rstrip().strip())
	
	if salvar == " ":
		print('\n')
		print(Colorir.RED2+dt[0]+" : "+Colorir.GREEN+dd[0]+Colorir.ENDC)
		print(Colorir.RED2+dt[1]+" : "+Colorir.GREEN+dd[1]+Colorir.ENDC)
		print(Colorir.RED2+dt[2]+" : "+Colorir.GREEN+dd[2]+Colorir.ENDC)
		print(Colorir.RED2+dt[3]+" : "+Colorir.GREEN+dd[3]+Colorir.ENDC+"\n")
		print(Colorir.RED2+"link: "+Colorir.GREENUNDER+link+Colorir.ENDC)
		print('\n')
		time.sleep(3)
	else:
		arq  = open("Vagas/"+salvar)
		temp = arq.readlines()
		temp.append(Mensagem.resultado.format(Empresadt=dt[0],Empresadd=dd[0],Salariodt=dt[1],Salariodd=dd[1],Cidadedt=dt[2],Cidadedd=dd[2],Descricdt=dt[3],Descricdd=dd[3],url=link))
		arq = open("Vagas/"+salvar,"w+")
		arq.writelines(temp)
		arq.close()

#buscando as vargas disponivel
##################################################################################
def procurar(cidade,estado,emprego,salvar):
	link ="http://www.sine.com.br/vagas-empregos-em-"+cidade+"-"+estado+"/"+emprego
	try:
		soup = BeautifulSoup(urlopen(link),"html.parser")
		
	except ConnectionResetError:
		time.sleep(5)
		soup = BeautifulSoup(urlopen(link),"html.parser")
		print("Tentando conectar novamente!")
		
	links = soup.find("div",{"class":"row jobs"}).find_all("a")
	if len(links) != 0:
		for row in links:
			mostraremprego(row.attrs["href"],salvar)
	else:
		print(Mensagem.EmpregoNot.format(url=link))

#Menu Lista
###################################################################################
def busca_emprego(Emprego):
	url  = "http://www.sine.com.br"+Emprego
	soup = BeautifulSoup(urlopen(url),"html.parser")
	links= soup.find("div",{"class":"row jobs"}).find_all("a")
	if not len(links) == 0:
		for row in links:
			mostraremprego(row.attrs["href"],salvar=" ")		

def busca_funcao(complemento_link):
	url   = "http://www.sine.com.br"+complemento_link
	soup  = BeautifulSoup(urlopen(url),"html.parser")
	links = soup.find("div",{"id":"ctl00_cphConteudo_pnlFuncao"}).find_all("a")
	lista_vagas = dict()
	for link in links:
		print(Colorir.GREEN+link.get_text()+" | Digite: "+Colorir.RED2+link.attrs["href"].split("/")[-1]+Colorir.ENDC)
		lista_vagas[link.attrs["href"].split("/")[-1]] = link.attrs["href"]
	
	escolha =str(input(Colorir.RED2+"\nQual você deseja escolher? "+Colorir.GREEN)).lower()
	if escolha in lista_vagas:
		busca_emprego(lista_vagas[escolha])
	else:
		print("Tente Novamente")
	
def busca_area():
	url ="http://www.sine.com.br/busca-de-vagas-area"
	soup  = BeautifulSoup(urlopen(url),"html.parser")
	links = soup.find("div",{"id":"ctl00_cphConteudo_pnlArea"}).find_all("a")
	lista_area = dict()
	 
	for link in links:
		print(Colorir.GREEN+link.get_text()+" | Digite: "+Colorir.RED2+link.attrs["href"].split("/")[-1]+Colorir.ENDC)
		lista_area[link.attrs["href"].split("/")[-1]] = link.attrs["href"]
		
	escolha =str(input(Colorir.RED2+"\nQual você deseja escolher? "+Colorir.GREEN)).lower()
	if escolha in lista_area:
		busca_funcao(lista_area[escolha])
	else:
		print("Tente Novamente")


#Menu interativo
########################################################################
def mainInterativo():
	while True:
		try:
		
			Cidades  = str(input(Colorir.RED+"\nExemplos:"+Colorir.GREEN+" Crato/CE,Juazeiro-do-Norte/CE\nDigite os nomes das Cidades: "+Colorir.ENDC) or (print(Colorir.YELLOW+"\nNão pode deixar esse campo vazio \nTente novamente!\n"+Colorir.ENDC),time.sleep(3))).lower().replace(" ","-").split(",")
			Empregos = str(input(Colorir.RED+"\nExemplos:"+Colorir.GREEN+" Desenvolvedor,Estagiario ou pode deixar vázio para mostrar as vagas recente\nDigite os nomes dos Empregos: "+Colorir.ENDC) or (print(Colorir.YELLOW+"\n Mostrar as Vagas Recentes\n"+Colorir.ENDC),time.sleep(3))).lower().replace(" ","-").split(",")
			Salvar   = str(input(Colorir.GREEN+"\nDeseja Salvar? S/n "+Colorir.ENDC).lower())
			
			if Salvar == "s" or Salvar == "sim":
				if "Vagas" not in os.listdir():
					os.mkdir("Vagas")
				Salvar = str(input(Colorir.RED+"exemplos: "+Colorir.GREEN+"programador.txt ou estagiario.txt\nDeseja Salvar aonde? "+Colorir.ENDC) or "sineEmpregos.txt")
				arq = open("Vagas/"+Salvar,"w+")
				arq.writelines(Mensagem.author) 
				arq.close()
			
			elif Salvar == "n" or Salvar == "nao" or Salvar == "não":
				Salvar = " "

			else:
				print(Mensagem.Novamente)
				mainInterativo()
			
			if not Cidades == "" and not Empregos == "":
				for cidade in Cidades:
					cidade,estado = cidade.split("/")[0],cidade.split("/")[1]
					for emprego in Empregos:
						procurar(cidade,estado,emprego,Salvar)
		
			parar = str(input(Colorir.GREEN+"Deseja fazer outra pesquisa? S/n "+Colorir.ENDC).lower())
			if parar == "s" or parar == "sim":
				pass
			else:
				print(Colorir.RED2+"\nSaindo!\n"+Colorir.ENDC)
				time.sleep(2)
				break
		except KeyboardInterrupt:
			print(Mensagem.Cancelado)
			break
		except IndexError:
			print(Mensagem.errorEstado)
			time.sleep(3)
		except NameError:
			print(Mensagem.errorBeautifulSoup)
			time.sleep(3)
			exit(1)
#######################################################################
def main():
	parser = argparse.ArgumentParser(prog="./pysine",description=" Esse script foi feito para fazer busca de emprego do jeito rápido e eficaz")
	parser.add_argument("-c","--cidades", default=" ", help="Pode colocar mais de uma cidade separado por vírgula, Exemplo: -c Recife/PE,Fortaleza/CE  ")
	parser.add_argument("-e","--empregos",default=" ", help="Pode colocar mais de um emprego separado por vígula,  Exemplo: -s Estagiario,desenvolvedor")
	parser.add_argument("-s","--salvar",  default=" ", help="Para salvar os resultados")
	parser.add_argument("-i","--interativo", action="store_true",help="Entrar no Modo Interativo")
	parser.add_argument("-l","--lista", action="store_true",help="Mostrar a lista das vagas de empregos disponivel")
	args = parser.parse_args()
	
	
	try:
		Cidades    = list(args.cidades.lower().split(","))
		Empregos   = list(args.empregos.lower().split(","))
		Salvar     = args.salvar.lower()
		Interativo = args.interativo
		Lista      = args.lista
		
		if Interativo:
			mainInterativo()
		
		elif Lista:
			busca_area()
		else:
			if not Salvar == " ":
				if "Vagas" not in os.listdir():
					os.mkdir("Vagas")
				arq = open("Vagas/"+Salvar,"w+")
				arq.writelines(Mensagem.author) 
				arq.close()
				
			if (not Cidades == " ") and (not Empregos == " "):
				for cidade in Cidades:
					cidade,estado = cidade.split("/")[0],cidade.split("/")[1]
					for emprego in Empregos:
						procurar(cidade,estado,emprego,Salvar)
			
	except UnicodeEncodeError:
		print(Mensagem.errorAcento)
		time.sleep(5)
		parser.print_help()
	except IndexError:
		print("IndexError")
		print(Mensagem.exemplos)
		time.sleep(5)
	except KeyboardInterrupt:
		print(Colorir.YELLOW+"\nCancelado com sucesso\n"+Colorir.ENDC)
		time.sleep(3)
	
	
if __name__ == "__main__":
	main()
