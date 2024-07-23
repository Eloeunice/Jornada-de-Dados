# ARQUIVO PARA FAZER OS TESTES DOS EXERCÍCIOS
numeros =[4,5,6,7,8]
for num in numeros:
   while num not in [0,1]:
     num -= 1 
   numeros.append(num)
print(numeros)
