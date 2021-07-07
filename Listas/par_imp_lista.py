n = int(input())
lista = list()
parid = [0, 0]
for i in range(n):
    lista.append(int(input()))
for j in lista:
    if j % 2 == 0:
        parid[0] += 1
    else:
        parid[1] += 1
print(parid[0])
print(parid[1])