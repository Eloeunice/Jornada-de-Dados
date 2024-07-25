
lista_alunos = ['joao', 'pedro', 'marcos']
id = 0
for aluno in lista_alunos:
    print(f'Aluno:{id} - {aluno}')
    id += 1

# Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma:

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i]) # sendo i a posição e a[i] a string 