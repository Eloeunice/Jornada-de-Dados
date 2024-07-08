# #### try-except e if
import ast

# 21: Conversor de Temperatura
try:
    temp_celsius = float(input("Digite a temperatura em celsius:"))
    temp_f = temp_celsius * 1.8 + 32
    print(temp_f)
except:
    print('O valor colocado não é do tipo float')

# 22: Verificador de Palíndromo

# desafio 053- Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
# (de tras pra frente é igual),
#desconsiderando os espaços:')
# obter uma entrada
frase = input('Digite uma frase:').upper().strip()

#fazer uma lista com as palavras da frase
lista = frase.split()

#juntar todas as letras em espaço
lista_junta = ''.join(lista)

#criar a frase inversa
frase_inversa = ''
#ler a frase de trás pra frente
for i in range(len(lista_junta)-1, -1, -1):
   frase_inversa += lista_junta[i]
if frase_inversa == lista_junta:
    print('TEMOS UM PALÍNDROMO')
else:
    print("ISSO NÃO É UM PALÍNDROMO")


#começa do começo, vai até o fim lendo de trás pra frente


# 23: Calculadora Simples
try:
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    op = int(input('Qual o operação você quer fazer: (1)ADIÇÃO/(2)SUBTRAÇÃO/(3)DIVISÃO/(4)MULTIPLICAÇÃO)'))
    if op == 1:
        print(f'Resultado: {num1 + num2}')
    elif op == 2:
        print(f'Resultado: {num1 - num2}')
    elif op == 3:
        if num2 == 0:
            print('Não é possível realizar a divisão por zero')
        else:
            print(f'Resultado: {num1 / num2}')
    elif op == 4:
        print(f'O Resultado: {num1 * num2}')
except:
    print('VALOR INVÁLIDO')


# 24: Classificador de Números
try:
    numero = input('Digite o número para ser classificado:')
    numero_real = ast.literal_eval(numero)  #converter a string em objeto

    if isinstance(numero_real, float):
        print("Esse número é do tipo float")
    elif isinstance(numero_real, int):
        print('Esse número é do tipo inteiro')
except:
    print('VALOR INVÁLIDO')


# 25: Conversão de Tipo com Validação
try:
    number = int(input('Digite um número inteiro:'))
    if number == int:
        print('Esse número é inteiro')
    else:
        print('Esse número não é inteiro')
except:
    print('VALOR INVÁLIDO')
finally:
    print('Fim do programa')

