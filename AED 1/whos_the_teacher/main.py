vetor_entradas = []
saida = -1

n = int(input())

professor = "0" * n

for x in range(n):
    vetor_entradas.append(input())

for index, element in enumerate(vetor_entradas):
    if professor in element:
        saida = index 

print(saida) 
