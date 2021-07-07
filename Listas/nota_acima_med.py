qtn = int(input())
nome = list()
notas = list()
for i in range(qtn):
    nome.append(input())
    notas.append(float(input()))
med = sum(notas) / len(notas)
for j in range(len(notas)):
    if notas[j] > med:
        print(nome[j])