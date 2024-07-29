# Aula 04

# O Pyhton tem a tipagem dinâmica e forte, o que significa que ele reconhece o tipo de dado enquanto o código está sendo executado

# Type hint é a "dica de tipo", serve pra indicar o tipo de dado que uma variável vai receber

idade: int = 30

# Listas
livros: list = ["Bíblia","O Corpo Guarda as Marcas","Arriscando a própria pele"]

# Dicionário

#chave : valor

carrinho: dict ={
    'produto': 'Camisa',
    'tamanho': 'p',
    'quantidade': 2,
    'preco': 25.0,
}

# LENDO ARQUIVOS

import csv 

# passo o caminho do arquivo
caminho_arquivo: str = 'aulas/aula04.py/arquivo.csv'

# crio uma variavel que recebe o documento
doc: list = []

# abro o arquivo
with open(file=caminho_arquivo,mode='r', encoding='utf-8') as arquivo:

 # leio o arquivo
 leitor_csv: csv.DictReader = csv.DictReader(arquivo)

 # coloco as linhas do arquivo dentro da variavel
 for linha in leitor_csv:
  doc.append(linha)

# mostro o arquivo
print(doc)

# FUNÇÕES

def soma(a: int, b:int) -> int:
 c = a + b
 return c
 
print(soma(10, 20))