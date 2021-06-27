estoque = int(input())
n_pedidos = int(input())
ped_atendidos = 0
c = 0 
while c < n_pedidos:
    qtn_produtos = int(input())
    if qtn_produtos <= estoque:
        ped_atendidos += 1
        estoque -= qtn_produtos
    c += 1
print(ped_atendidos)