n = int(input())
lista = list()
soma = 0
for i in range(n):
    lista.append(int(input()))
qtn_1 = lista.count(1)
for j in range(qtn_1):
    pos = lista.index(1)
    if (pos-1) >= 0:
        soma += lista[pos-1] 
    if (pos + 1) <= (len(lista) - 1) :
        soma += lista[pos+1]
    lista.pop(pos)
print(soma)