# pysine
Ferramenta desenvolvida para auxiliar o pessoal a procurar empregos do jeito (Rápido|inteligente) no </br>[Sine](http://www.sine.com.br)

------------------------------------------------------------------------------------------------------
# Install no Linux
passo 1:
instale o python 3.5 https://www.python.org/downloads/


passo 2:
Entra no shell e digite

`mkdir pysine; cd pysine
`git clone https://github.com/EricksonDouglas/Pysine.git

passo 3:
Instale a dependecia com o pip
`pip install -r requisitos.txt

# Install no Windows
Tutorial vai sair em breve!

------------------------------------------------------------------------------------------------------
# Uso

usage: ./pysine [-h] [-c CIDADES] [-e EMPREGOS] [-s SALVAR] [-v]

[+] Modo Interativo
`./pysine 

[+] Mostrando o resultado do emprego Estagiario na Cidade Crato/PE
`python3 pysine -e Estagiario --cidades Crato/CE -v

[+] Salvando o resultado dos empregos da cidade Juazeiro do norte no arquivo vendedor.txt 
`./pysine -c juazeiro-do-norte/ce --empregos Vendedor,vendedor-externo --salvar vendedor.txt

[+] Criando e Salvando resultado dos empregos nas Cidades Fortaleza/CE e Recife/pe no arquivo programador.txt dentro da pasta empregos 
`python3 pysine -c FORTALEZA/CE,recife/pe -e web-programador,desenvolvedor,analista-desenvolvimento-de-sistemas -s ~/empregos/programador.txt