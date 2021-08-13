"""
Enunciado:
    - Dado um paciente novo, pesquisando na base de dados qual o paciente com os sintomas mais parecidos e sugerir seu diagnóstico como provável

Atividade:
    - Dado um paciente novo, pesquisando na base de dados quais os 3 pacientes com sintomas mais parecidos e sugerir o diagnóstico majoritário (ou favorecendo diagnóstico positivo por segurança) como provável

"""
import numpy as np

def dist(paciente1, paciente2):
  soma = 0
  for i in range(len(paciente1)):
    soma += (paciente1[i] - paciente2[i]) ** 2
  return soma ** (1/2)

def dist_base(base, paciente):
  distancias = list()
  for i in base:#range(len(base))
    distancias.append(dist(paciente, i[:-1]))
  return(distancias)

def diagnostico(paciente, base):
  distancias = dist_base(base, paciente)
  #distancias.index(min(distancias))
  dist_np = np.array(distancias)
  return(base[dist_np.argmin()][-1])

#Se algum dos 3 que forem proximos de um infectado, então conta como infectado, retornando 1
def diagnostico2(paciente, base):
  distancias = dist_base(base, paciente)
  dist_np = np.array(distancias)
  aux = dist_np.argsort()
  for i in range(3):
    if base[aux[i]][-1] == 1:
      return 1
  return 0

def main():
  #fonte: https://www.nature.com/articles/s41746-020-00372-6

  rotulos = ['cough', 'fever', 'sore_throat', 'shortness_of_breath', 'head_ache', 'age_60_and_above', 'gender', 'test_indication',  'corona_result']

  base = [[0,0,0,0,0,0,1,2,1], 
          [0,0,0,0,0,0,1,2,1], 
          [0,0,0,0,0,1,1,0,1], 
          [0,0,0,0,0,0,1,0,1], 
          [0,0,0,0,0,0,0,0,1], 
          [0,0,0,0,0,0,1,0,1], 
          [1,1,0,0,0,1,1,0,1], 
          [0,0,0,0,0,0,1,0,1], 
          [1,0,0,0,0,0,0,0,1], 
          [0,0,0,0,0,0,1,0,1], 
          [0,1,0,0,0,0,0,2,0], 
          [0,0,0,0,0,0,1,2,0], 
          [1,0,0,0,0,0,0,2,0], 
          [0,0,0,0,0,1,0,2,0], 
          [1,1,0,0,0,0,1,1,0], 
          [0,0,0,1,0,1,0,1,0], 
          [0,0,0,0,0,0,0,1,0], 
          [1,1,0,0,0,0,0,1,0], 
          [1,0,0,0,0,0,0,1,0], 
          [1,0,0,0,0,0,1,1,0]]

  novo1 = [1,0,0,0,0,0,0,1] #0
  novo2 = [0,0,0,0,0,0,1,2] #1

  #print(diagnostico(novo1, base))
  #print(diagnostico(novo2, base))

  print(diagnostico2(novo1, base))
  print(diagnostico2(novo2, base))

main()