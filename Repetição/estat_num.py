n = int(input())
numeros = []
for i in range(n):
    num = int(input())
    numeros.append(num)
print(sum(numeros))
print(sum(numeros)/len(numeros))
print(min(numeros))
print(max(numeros))