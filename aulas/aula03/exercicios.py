### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

preco = float(input("Qual o preço do produto?R$"))
qnt = int(input("Quantos foram comprados?"))
if preco > 0 and qnt > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'
temperatura = float(input("Temperatura:"))
if temperatura < 18:
    print("Baixa")
elif 18 <= temperatura <= 26:
    print("Normal")
else:
    print("Alta")

    
### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log.get('level') == 'ERROR': # *log['level'] == 'ERROR'
    print(log.get('message'))

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input('Digite sua idade:'))
email = input('Digite seu email:')
while True:
    if 18 < idade > 65:
     print('A sua idade não está está entre 18 e 65 anos')
    if '@' not in email:
      print('O seu email não possui um @')
    else:
     print('Dados de usuário válidos')
    break

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

valor = float(input('Qual o valor da transacao:'))

hora = int(input('Qual a hora da transacao:'))

transacao = {'valor': valor, 'hora': hora}

if transacao['valor'] > 10000 or 9 > transacao['hora'] > 18:
   print('Transacao suspeita')
   
### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

count = {} # Dicionario que vai receber a contagem das palavras
texto = input('Digite um texto:') # recebe o texto a ser analisado
palavras = texto.split(' ') # lista das palavras
for palavra in palavras: # para cada palavra da lista de palavras
    if palavra in count: # se a palavra estiver no dicionario
        count[palavra] += 1 # soma 1 na conta dessa palavra
    else: # se nao estiver no dicionario
        count[palavra] = 1 # a contagem dela é um
print(palavra, count) # mostra a palavra e quantas vezes ela apareceu 

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros =[4,5,6,7,8]
for num in numeros:
   while num not in [0,1]:
    num -= 1 
   numeros.append(num)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

dados = [{'nome': 'Maria', 'email': 'maria@gmail.com'},
   {'nome': 'João', 'email': 'joao@gmail.com'},
   {'nome': 'Pedro', 'email': ''},
   {'nome': 'Lucas', 'email': 'lucas@hotmail.com'}]
          
usuarios_validos = [usuario for usuario in dados if usuario["email"]]
# usuarios validos recebem a lista de usuario para os usuarios na lista de dados se o usuario tem email

print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = [1,2,3,4,5,6,7,8,9]
for num in numeros:
   if num % 2 == 0:
      print(num)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

# CRIO O DICIONARIO QUE VAI RECEBER RESULTADO FINAL

total_por_categoria = {} #var que armazena o valor total pela categoria

# PASSO PELO DICIONARIO VERIFICANDO CADA VENDA E VOU GUARDANDO A CATEGORIA E O VALOR DE CADA UMA

for venda in vendas: #para cada venda 
    categoria = venda["categoria"] #a categoria vai receber a categoria que foi armazenada na lista de vendas
    valor = venda["valor"] #valor recebe o valor que foi armazenado na lista de vendas

    if categoria in total_por_categoria: # se a categoria esta no dicionario que aramzena os resultados
        total_por_categoria[categoria] += valor # voce soma o valor denovo
    else:
        total_por_categoria[categoria] = valor #senao permanece com o unico valor salvo mesmo

print(total_por_categoria)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
word = str

while word != 'sair':
   word = input('Digite uma palavra:')
print('saindo..')

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
num = int

while num not in [14,15,16,18,19]:
   num = int(input('Digite um número entre 14 e 19:'))

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
pagina_inicial =1
pagina_final = 2

while pagina_inicial <= pagina_final:
   print(f'Processando pagina {pagina_inicial} de {pagina_final}')
   time.sleep(1)
print('Terminado')
### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

import time
tent = 0
conex = False

while tent < 5:
   conex = False
   tent += 1
   time.sleep(1)
   print(f'tentativas:{tent} conexão:{conex}')

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = ['maca', 'banana', 'chocolate', 'bicicleta', 'pipoca', 'chinelo']

i = 0
while i < len(lista):
   if lista[i] == 'chinelo':
      print('Valor encontrado!')
      break
   print(f'{lista[i]}')
   i += 1