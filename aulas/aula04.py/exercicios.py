#Exercícios de Listas e Dicionários
import math
#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numeros: list = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(math.pow(numero,2))

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

linguagens: list = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros: dict = {
    'titulo': 'Senhor dos Anéis',
    'autor': 'J.R.R. Tolkien',
    'ano_publicacao': 1937
}

info_livros = livros.items()
for info in info_livros:
 print(info)

print(livros.get('titulo'))

 # livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
#for chave, valor in livro.items():
    #print(f"{chave}: {valor}")

#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

frase = "o valor do amor é eterno" 
letras = {} #dicionario que vai receber as letras
for letra in frase: # para cada letra na frase
   if letra in letras: # se a letra já existe no dicionario
     letras[letra] += 1
   else: # se a letra não existe no dicionario
      letras[letra] = 1
print(letras)
   
#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

frutas: list= ["maçã", "banana", "cereja"]
preco = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total = 0 # total = sum(precos[item] for item in lista_compras)
for p in preco.values():
   total += p
print(total)

 #Eliminação de Duplicatas Objetivo: Dada uma lista de emails, remover todos os duplicados.

# Filtragem de Dados Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# Ordenação Personalizada Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# Ordenação Personalizada Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# Divisão de Dados em Grupos Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# EXERCICIOS COM DICIONARIOS

# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# Dados dois dicionários, fundi-los em um único dicionário.

# Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# Dado um dicionário, criar listas separadas para suas chaves e valores.

# Dada uma string, contar a frequência de cada caractere usando um dicionário.