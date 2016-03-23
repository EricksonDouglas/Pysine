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

import time,argparse
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

#Adicionando mensagens na variavel
######################################################################
author   = """

											  
[+]	Author:   Erickson Douglas				  
[+]	Facebook: erickshow.mattos
[+]	Twitter:  @erickshowplay 

"""
exemplos = Colorir.GREEN+"""
Exemplos

[+] Modo Interativo
"""+Colorir.BRED+"""./pysine
"""+Colorir.GREEN+"""[+] Mostrando o resultado do emprego Estagiario na Cidade Crato/PE
"""+Colorir.BRED+"""python3 pysine -e Estagiario --cidades Crato/CE -v

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
		
	for row in soup.find("dl",{"class":"dl-horizontal"}).find_all("dt"):
		dt.append(row.get_text().rstrip().strip())
		
	for row in soup.find("dl",{"class":"dl-horizontal"}).find_all("dd"):
		dd.append(row.get_text().rstrip().strip())
	
	if salvar == " ":
		print(Colorir.YELLOW+">"*100+Colorir.ENDC+'\n')
		print(Colorir.RED2+dt[0]+" : "+Colorir.GREEN+dd[0]+Colorir.ENDC)
		print(Colorir.RED2+dt[1]+" : "+Colorir.GREEN+dd[1]+Colorir.ENDC)
		print(Colorir.RED2+dt[2]+" : "+Colorir.GREEN+dd[2]+Colorir.ENDC)
		print(Colorir.RED2+dt[3]+" : "+Colorir.GREEN+dd[3]+Colorir.ENDC+"\n")
		print(Colorir.RED2+"link: "+Colorir.GREENUNDER+link+Colorir.ENDC)
		print('\n'+Colorir.YELLOW+"<"*100+Colorir.ENDC)
		time.sleep(3)
	else:
		arq  = open(salvar)
		temp = arq.readlines()
		temp.append(resultado.format(Empresadt=dt[0],Empresadd=dd[0],Salariodt=dt[1],Salariodd=dd[1],Cidadedt=dt[2],Cidadedd=dd[2],Descricdt=dt[3],Descricdd=dd[3],url=link))
		arq = open(salvar,"w+")
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
		print(Colorir.WARNING+"[-]"+">"*50)
		print("[-] Emprego não encontrado: ")
		print("[-]"+"<"*50+Colorir.ENDC)
		print(Colorir.RED2+"Link: "+Colorir.GREEN+link+Colorir.ENDC)

#Menu interativo
########################################################################
def mainInterativo():
	while True:
		try:
		
			Cidades  = str(input(Colorir.RED+"\nExemplos:"+Colorir.GREEN+" Crato/CE,Juazeiro-do-Norte/CE\nDigite os nomes das Cidades: "+Colorir.ENDC) or (print(Colorir.YELLOW+"\nNão pode deixar nenhum campo vazio\nTente novamente!\n"+Colorir.ENDC),time.sleep(3))).lower().replace(" ","-").split(",")
			Empregos = str(input(Colorir.RED+"\nExemplos: Desenvolvedor,Estagiario\n"+Colorir.GREEN+"Digite os nomes dos Empregos: "+Colorir.ENDC) or (print(Colorir.YELLOW+"\nNão pode deixar nenhum campo vazio\nTente novamente!\n"+Colorir.ENDC),time.sleep(3))).lower().replace(" ","-").split(",")
			Salvar   = str(input(Colorir.GREEN+"\nDeseja Salvar? S/n "+Colorir.ENDC).lower())
			
			if Salvar == "s" or Salvar == "sim":
				Salvar = str(input(Colorir.RED+"exemplos: "+Colorir.GREEN+"programador.txt ou estagiario.txt\nDeseja Salvar aonde? "+Colorir.ENDC) or "sineEmpregos.txt")
				arq = open(Salvar,"w+")
				arq.writelines(author) 
				arq.close()
			
			elif Salvar == "n" or Salvar == "nao" or Salvar == "não":
				Salvar = " "

			else:
				print(Colorir.YELLOW+"\nTente novamente\n"+Colorir.ENDC)
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
			print(Colorir.YELLOW+"\nCancelado com Sucesso\n"+Colorir.ENDC)
			break
		except IndexError:
			print(Colorir.YELLOW+"\nEsqueceu colocar o Estado, exemplos:Bodoco/pe, juazeiro-do-norte/CE\nTente novamente "+Colorir.ENDC)
			time.sleep(3)
		except NameError:
			print(Colorir.YELLOW+'''
____________________________________
BeautifulSoup4 não instalado
Faça a instalação do BeautifulSoup
[+] pip install -r requisitos.txt

'''+Colorir.ENDC)
			time.sleep(3)
			exit(1)
#######################################################################
def main():
	parser = argparse.ArgumentParser(prog="./pysine",description=" Esse script foi feito para fazer busca de emprego do jeito rápido e eficaz")
	parser.add_argument("-c","--cidades", type=str, help="Pode colocar mais de uma cidade separado por vírgula, Exemplo: -c Recife/PE,Fortaleza/CE  ")
	parser.add_argument("-e","--empregos",type=str, help="Pode colocar mais de um emprego separado por vígula,  Exemplo: -s Estagiario,desenvolvedor")
	parser.add_argument("-s","--salvar", default=" ", help="Para salvar os resultados")
	args = parser.parse_args()
	
	
	try:
		Cidades    = list(args.cidades.lower().split(","))
		Empregos   = list(args.empregos.lower().split(","))
		Salvar     = args.salvar.lower()
		
		
		if not Salvar == " ":
			arq = open(Salvar,"w+")
			arq.writelines(author) 
			arq.close()
			
		if not Cidades == "" and not Empregos == "":
			for cidade in Cidades:
				cidade,estado = cidade.split("/")[0],cidade.split("/")[1]
				for emprego in Empregos:
					procurar(cidade,estado,emprego,Salvar)
	
	except AttributeError:
		print("\n\nEntrando -> modo Interativo <-\n")
		time.sleep(2)
		mainInterativo()
	except UnicodeEncodeError:
		print(errorAcento)
		time.sleep(5)
		parser.print_help()
	except IndexError:
		print(exemplos)
		time.sleep(5)
		print(Colorir.YELLOW+"\nEsqueceu colocar o Estado, exemplos:Bodoco/pe, juazeiro-do-norte/CE\nTente novamente "+Colorir.ENDC)
	except KeyboardInterrupt:
		print(Colorir.YELLOW+"\nCancelado com sucesso\n"+Colorir.ENDC)
		time.sleep(3)
		parser.print_help()
	
	
if __name__ == "__main__":
	main()
