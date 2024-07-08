### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome = input('Digite o seu nome:')
if nome.isnumeric():
    print("Nome inválido!")
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite seu salario:"))
except:
    print("Valor inválido!")
    exit()  # tem que sair e encerrar o programa se não ele vai continuar sem os dados

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus = float(input('Digite o bonus em porcentagem:'))
except:
    print("Valor inválido!")
    exit()

# 4) Calcule o valor do bônus final
valor_final = salario + salario * (bonus/100)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá {nome}, o seu salário com o bônus é de {valor_final:.2f} reais')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
     #O usuário pode digitar um número no nome
