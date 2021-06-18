"""
Controle do cartão de crédito
Opções de uso:
- Compra
- Consulta limite
- Paga fatura (reinicia limite)
- Aumenta limite (exige autenticação por senha com 3 tentativas)

Atividade:
– A opção de compra deve permitir que seja inserida a categoria (supermercado, entretenimento ou
diversos)
- Deve ser adicionada uma opção que exibe estatísticas sobre gastos em cada categoria (% dos gastos em supermercado, etc)
"""

import datetime

def compra(limite, fatura):
  valor = float(input("Qual o valor da compra? "))
  if valor <= limite:
    limite -= valor
    fatura += valor
  else:
    print("Compra não efetuada, limite insuficiente")
  return limite, fatura

def aumenta_limite(senha_correta, senha_bloqueada, bloqueio):
  if (senha_bloqueada and (datetime.datetime.now() - bloqueio).seconds < 30):
    print("Senha bloqueada")
    return 0, bloqueio
  else:
    limite_aumento = float(input("Qual o aumento de limite? "))
    senha = input("Digite a senha: ")
    tentativas = 1
    while (tentativas <= 2 and senha != senha_correta):
      senha = input("Senha incorreta, tente novamente: ")
      tentativas += 1
    if(senha ==  senha_correta):
      return limite_aumento, datetime.datetime.now()
    else:
      print("Senha incorreta, tentativas esgotadas")
      return 0, datetime.datetime.now()


def main():
  #limite_inicial = 1000
  #limite = limite_inicial
  limite = limite_inicial = 1000
  senha = "1234"
  fatura = 0
  senha_bloqueada = False
  bloqueio = datetime.datetime.now()

  opcao = input("1 - Compra|2 - Consultar limite|3 - Pagar fatura|4 - Aumentar limite|0 - Sair:\n")

  while opcao!="0":
    if opcao == "1":
      limite, fatura = compra(limite, fatura)
    elif opcao == "2":
      print("Seu limite restante é " + str(limite))
    elif opcao == "3":
      print("Sua fatura é: " + str(fatura))
      limite = limite_inicial
      fatura = 0
    elif opcao == "4":
      aumento, bloqueio = aumenta_limite(senha, senha_bloqueada, bloqueio)
      if aumento == 0:
        senha_bloqueada = True
      else:
        senha_bloqueada = False
      limite += aumento
      limite_inicial += aumento

    opcao = input("1 - Compra|2 - Consultar limite|3 - Pagar fatura|4 - Aumentar limite|0 - Sair:\n")  

main()
