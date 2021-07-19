def verifica(lista):
    ver = 0
    for j in range(len(lista)):
        aux = -(j + 1)
        if lista[j] != lista[aux]:
            ver += 1
    if ver != 0:
        return "NAO"
    return "SIM"

def main():
    n = int(input())
    lista = list()
    for i in range(n):
        lista.append(int(input()))
    print(verifica(lista))
    
main()