### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = ['maca', 'banana', 'chocolate', 'bicicleta', 'pipoca', 'chinelo']

i = 0
while i < len(lista):
   if lista[i] == 'chocolate':
      print('Valor encontrado!')
      break
   print(f'{lista[i]}')
   i += 1
   
