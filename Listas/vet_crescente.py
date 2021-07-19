n = int(input())
lista1 = list()
for i in range(n):
    lista1.append(int(input()))
lista2 = lista1.copy()
lista2.sort()
if lista1 == lista2:
    print("SIM")
else:
    print("NAO")