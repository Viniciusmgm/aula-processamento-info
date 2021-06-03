salario = float(input())
vendas = float(input())
comis = vendas * 0.2
print(f'{comis:.02f}')
if (comis >= (salario / 2)):
    print("Atingiu meta de vendas")
else:
    print("Nao atingiu meta de vendas")   