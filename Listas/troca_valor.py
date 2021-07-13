def troca(i,j,lista):
    if (i >= 0 and j >= 0) and (i <= (len(lista) - 1) and j <= (len(lista) - 1)):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
    return lista

def main():
    n = int(input())
    lista = []
    for k in range(n):
        lista.append(int(input()))
    i = int(input())
    j = int(input())
    lista = troca(i,j,lista)
    for h in lista:
        print(h)
    
main()