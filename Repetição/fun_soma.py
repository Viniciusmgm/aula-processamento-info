def fun_soma(n):
    soma = 0
    for i in range(1,n+1):
        for j in range(1,9):
            soma += (i + 1) * j
    print(soma)

def main():
    n = int(input())
    fun_soma(n)
    
main()