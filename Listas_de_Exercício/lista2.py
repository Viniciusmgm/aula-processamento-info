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
