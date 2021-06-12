#Lista 1

#Exercício 1
#a)Algoritmo:
"""
Entrada: posições de x e y da flecha
Saída: posição da flecha no alvo 
"""

#b)Código em Python:
"""
def posicao(x,y):
  if((x <= 1 and x >= -1) and (y <= 1 and y >= -1)):
    return "A flecha atingiu a região A"
  elif((x <= 2 and x >= -2) and (y <= 2 and y >= -2)):
    return "A flecha atingiu a região B"
  elif((x <= 3 and x >= -3) and (y <= 3 and y >= -3)):
    return "A flecha atingiu a região C"
  elif((x <= 4 and x >= -4) and (y <= 4 and y >= -4)):
    return "A flecha atingiu a região D"
  elif((x <= 5 and x >= -5) and (y <= 5 and y >= -5)):
    return "A flecha atingiu a região E"
  else:
    return "A flecha foi para fora do alvo"

def main():
  x = int(input("Qual a posição x da flecha? "))
  y = int(input("Qual a posição y da flecha? "))
  print(posicao(x,y))
main()
"""

#Exercício 2
"""

"""

