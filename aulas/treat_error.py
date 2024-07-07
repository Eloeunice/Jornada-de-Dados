#EXERCÍCIOS
import math
  #Inteiros (int)
#Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
sum = num1 + num2
print(sum)

#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num3 = int(input('Digite um número e eu te mostarei o resto da divisão desse número por 5:'))
resto = num3 % 5
print(resto)

#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num4 = int(input('Digite o primeiro número:'))
num5 = int(input('Digite o segundo número:'))
mult = num4 * num5
print(mult)

#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num6 = int(input('Digite o primeiro número:'))
num7 = int(input('Digite o segundo número:'))
divisao_inteira = num6 // num7
print(divisao_inteira)

#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num8 = int(input('Digite um número e eu te mostarei o quadrado desse número:'))
square = num8**2
print(square)

  #Números de Ponto Flutuante (float)
#Escreva um programa que receba dois números flutuantes e realize sua adição.
num9 = float(input('Digite o primeiro número:'))
num10 = float(input('Digite o segundo número:'))
sum_float = num9 + num10
print(sum_float)

#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num11 = float(input('Digite o primeiro número:'))
num12 = float(input('Digite o segundo número:'))
media = (num11 + num12) / 2
print(media)
#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input('Digite o número base:'))
exp = float(input('Digite o número expoente :'))
pot = base**exp
print(pot)

#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temp_celsius = float(input("Digite a temperatura em celsius:"))
temp_f = temp_celsius * 1.8 + 32
print(temp_f)
#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Escreva o número do raio:"))
area = math.pi * raio **2
print(area)
  #Strings (str)
#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
frase = input("Digite uma frase ou uma palavra:")
print(frase.upper())

#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input('Digite seu nome completo:')
print(nome.lower())

#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase2 = input("Digite uma frase ou uma palavra:")
print(frase2.strip())
#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input('Digite a data no formato "dd/mm/aaaa":')
print(data.split('/'))
#Escreva um programa que concatene duas strings fornecidas pelo usuário.
frase2 = input("Digite uma frase ou uma palavra:")
frase3 = input("Digite uma frase ou uma palavra:")
frases = frase2 + frase3
print(frases)

  #Booleanos (bool)
#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
resposta1 = bool(input(('Coloque uma expressao booleana:')))
resposta2 = bool(input(('Coloque uma expressao booleana:')))
print(resposta1 and resposta2)


#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
resposta3 = bool(input(('Coloque uma expressao booleana:')))
resposta4 = bool(input(('Coloque uma expressao booleana:')))
print(resposta3 or resposta4)


#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resposta5 = bool(input(('Coloque uma expressao booleana:')))
print(not resposta5)

#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
print(numero1 == numero2)

#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero3 = int(input('Digite o primeiro número:'))
numero4 = int(input('Digite o segundo número:'))
print(numero3!= numero4)
