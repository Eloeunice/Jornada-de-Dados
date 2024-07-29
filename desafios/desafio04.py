# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

### Desafio - Refatorar o projeto da aula anterior usando Dicionário, Type Hint e Funções

nome_valido = False
salario_valido = False
bonus_valido = False
 
infos = {}

while nome_valido is not True:
# 1) Solicita ao usuário que digite seu nome
    nome: str = input('Digite o seu nome:')
    if nome.isnumeric():
        print("Nome inválido!")
        continue
    else:
         nome_valido = True 
         infos['nome'] = nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
while salario_valido is not True: 
    try:
        salario: float = float(input("Digite seu salario:"))
        salario_valido = True
        infos['salario'] = salario
    except:
        print("Valor inválido!")
    
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
while bonus_valido is not True:
    try:
        bonus: float = float(input('Digite o bonus em porcentagem:'))
        bonus_valido = True
        infos['bonus'] = bonus
    except:
        print("Valor inválido!")


# 4) Calcule o valor do bônus final
def calculo_final(salario, bonus) -> float:
    valor_final: float = salario + salario * (bonus/100)
    return valor_final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá {nome}, o seu salário com o bônus é de {calculo_final(salario,bonus):.2f} reais')
print(infos)

