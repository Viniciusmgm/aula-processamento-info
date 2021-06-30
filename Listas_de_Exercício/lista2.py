#Exercício 1
#Ainda falta terminar
"""
import random

def pontuacao(tentativas,ponto_regiao):
  pontos = 0
  while tentativas > 0:
    x = random.uniform(-5,5)
    y = random.uniform(-5,5)
    dist = ((x ** 2) + (y ** 2)) ** 0.5
    pontos += posicao(dist, ponto_regiao)
    tentativas -= 1
  return pontos

def posicao(dist, ponto_regiao):
  if(dist <= 1):
    return ponto_regiao[0]
  elif(dist <= 2):
    return ponto_regiao[1]
  elif(dist <= 3):
    return ponto_regiao[2]
  elif(dist <= 4):
    return ponto_regiao[3]
  elif(dist <= 5):
    return ponto_regiao[4]
  else:
    return ponto_regiao[5]

def main():
  tentativas = int(input("Quantas tentativas deseja realizar? "))
  ponto_regiao = 10, 8, 6, 4, 2, 0
  print("Sua pontuação total foi de {} pontos ".format(pontuacao(tentativas,ponto_regiao)))
  
main()
"""

#Exercício 2
"""
a)
"""

#Exercício 3
"""
def tabuada(num):
  for j in range(1,11):
    print("\n")
    for i in range(2,num+1):
      print("{} x {} = {}".format(i, j, (i*j)), end = " ")

def main():
  num = int(input("Digite um número inteiro, para saber a tabuada até esse número: "))
  tabuada(num)

main()
"""

#Exercício 4
"""
def vezes(conceito,vezes_conceito):
  conceito = conceito.lower()
  if conceito == "a":
    vezes_conceito["A"] += 1
  elif conceito == "b":
    vezes_conceito["B"] += 1
  elif conceito == "c":
    vezes_conceito["C"] += 1
  elif conceito == "d":
    vezes_conceito["D"] += 1
  elif conceito == "f":
    vezes_conceito["F"] += 1
  else:
    vezes_conceito["O"] += 1

def main():
  continuar = "s"
  vezes_conceito = dict(A = 0, B = 0, C = 0, D = 0, F = 0, O = 0)
  while continuar == "s":
    conceito = input("Digite o conceito dos alunos: ")
    continuar = input("Deseja continuar colocando conceitos(s/n)? ")
    vezes(conceito,vezes_conceito)
  print("\nAs frequências com que os conceitos ocorreram foram: ")
  for i in vezes_conceito:
    print("{} = {} vezes".format(i,vezes_conceito[i]))

main()
"""
