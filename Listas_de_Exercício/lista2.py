#Exercício 1
"""
import random

#gera as coordenadas, calcula a distância e contabiliza os pontos
def pontuacao(tentativas, ponto_regiao):
  pontos = 0
  while tentativas > 0:
    x = random.uniform(-5,5)
    y = random.uniform(-5,5)
    dist = ((x ** 2) + (y ** 2)) ** 0.5
    pontos_rodada, regiao_atingida = posicao(dist, ponto_regiao)
    pontos += pontos_rodada
    tentativas -= 1
  return pontos, regiao_atingida

#verifica a regiao atingida
def posicao(dist, ponto_regiao):
  if(dist <= 1):
    return ponto_regiao["a"], "A"
  elif(dist <= 2):
    return ponto_regiao["b"], "B"
  elif(dist <= 3):
    return ponto_regiao["c"], "C"
  elif(dist <= 4):
    return ponto_regiao["d"], "D"
  elif(dist <= 5):
    return ponto_regiao["e"], "E"
  else:
    return ponto_regiao["f"], "fora do alvo"

def main():
  tentativas = int(input("Quantas tentativas deseja realizar? "))
  tentativas_espec = 0
  ponto_regiao = dict(a = 10, b = 8, c = 6, d = 4, e = 2, f = 0)
  pontos, regiao_atingida = pontuacao(tentativas,ponto_regiao)
  regiao_atingida = ""
  print("Sua pontuação total foi de {} pontos ".format(pontos))

  regiao_espec = input("Deseja acertar alguma região especifíca (s/n)? ")
  if regiao_espec == 's':
    regiao_espec = input("Qual seria essa região? ")
    #realiza a contagem das tentativas 
    while regiao_espec.upper() != regiao_atingida:
      pontos, regiao_atingida = pontuacao(tentativas,ponto_regiao)
      tentativas_espec += 1
    
    print("A região {} foi atingida após {} tentativa(s)".format(regiao_espec.upper(), tentativas_espec))

main()
"""

#Exercício 2
"""
a)Exemplo de contagem regressiva com for e while:
#Exemplo com while:
import time

num = int(input("De qual número quer começar a contagem regressiva ? "))
while num > 0:
  print(num)
  time.sleep(1)
  num -= 1
print("Parabéns !!!")

#Exemplo com for:
import time

num = int(input("De qual número quer começar a contagem regressiva ? "))
for i in range(num, 0, -1):
  print(i)
  time.sleep(1)
print("Parabéns !!!")

b) While é mais adequado quando não se sabe quantas vezes o laço vai se repetir, já o for é mais adequado quando se tem uma noção maior ou uma certeza de quantas vezes o laço vai se repetir
#Exemplo com for:
print("\t\t\t|----------Média do Aluno----------|\n")
qtn_notas = int(input("Quantas notas deseja colocar? "))
soma = 0
for i in range(qtn_notas):
  num = float(input("Digite a nota: "))
  soma += num
media = soma / qtn_notas
print("Sua média foi: {}".format(round(media,2)))

#Exemplo com while:
print("\t\t\t|----------Média do Aluno----------|\n")
continuar = input("Deseja continuar inserindo notas (s/n)? ")
soma = 0
qtn_notas = 0
while continuar.lower() == "s":
  num = float(input("Digite a nota: "))
  soma += num
  qtn_notas += 1
  continuar = input("Deseja continuar inserindo notas (s/n)? ")
media = soma / qtn_notas
print("Sua média foi: {}".format(round(media,2)))
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