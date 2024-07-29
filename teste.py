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