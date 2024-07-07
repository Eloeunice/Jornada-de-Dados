### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome = input('Digite o seu nome:')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu salario:"))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input('Digite o bonus em porcentagem:'))

# 4) Calcule o valor do bônus final
valor_final = salario + salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá {nome}, o seu salário com o bônus é de {valor_final:.2f} reais')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
     #O usuário pode digitar um número no nome
     #O bonus pode acabar sendo maior que o salario
