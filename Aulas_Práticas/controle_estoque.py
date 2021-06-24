"""
Enunciado
Criar um programa que gerencie as vendas de uma lojinha.
Funcionalidades:
- listar produtos e preços
- realizar uma venda

Atividade:
- Utilizar um outro dicionário parar armazenar o histórico de vendas (qtos itens de cada produto já foram vendidos)
- Criar uma 3a funcionalidade onde o usuário pode consultar qual é o produto mais vendido
"""

def mais_vendido(qtn):
  mais_vend = 0
  prod_mais = 0
  for i in qtn:
    if(qtn[i] >= mais_vend):
      mais_vend = qtn[i]
      prod_mais = i
  print("O produto mais vendido foi a(o) {}, que foi vendido(a) {} vezes".format(prod_mais,mais_vend))
   

def venda(precos,qtn):
  produto = "n"
  total = 0
  while (produto != "s"):
    produto = input("Digite o nome do produto (s para encerrar): ")
    if produto != "s":
      print("{}: R${:.2f}".format(produto, precos[produto]))
      total += precos[produto]
      if(produto == "bolsa"):
        qtn[produto] += 1
      elif(produto == "colar"):
        qtn[produto] += 1
      elif(produto == "pulseira"):
        qtn[produto] += 1
      elif(produto == "brinco"):
        qtn[produto] += 1
  print("Valor do carrinho: {:.2f}".format(total))
  return qtn

def main():
  precos = dict(bolsa = 30, colar = 20, pulseira = 15, brinco = 10)
  qtn = dict(bolsa = 0, colar = 0, pulseira = 0, brinco = 0)
  menu = "|1 - Listar produtos \n|2 - Realizar uma compra \n|3 - Consultar produto mais vendido \n|0 - Sair \n"
  opcao = 1

  #opcao = input(menu)
  while (opcao != "0"):
    opcao = input(menu)
    if opcao == "1":
      for produto in precos:
        print("{}: R${:.2f}".format(produto, precos[produto]))
    elif opcao == "2":
      qtn = venda(precos,qtn)
    elif opcao == "3":
      mais_vendido(qtn)
    #opcao = input(menu)
      
main()
