#Exercício 1
"""
def matriz_zeros(nlin, ncol):
  M_zeros = list()
  for i in range(nlin):
    linha = list()
    for j in range(ncol):
      linha.append(0)
    M_zeros.append(linha)
  return M_zeros

def transposta(M):
  nlin = len(M)
  ncol = len(M[0])
  Mt = matriz_zeros(nlin, ncol)
  for i in range(ncol):
    for j in range(nlin):
      Mt[i][j] = M[j][i]
  return Mt

def main():
  M = [[1,1,1],[1,1,1],[2,2,2]]
  Mt = transposta(M)
  if Mt == M:
    print("A matriz é simétrica")
  else:
    print("A matriz não é simétrica")
main()
"""

#Exercício 2
"""
def main():
  
main()
"""

#Exercício 3
"""
O n1 vai ser printado como 5, já a matriz terá um acréscimo na posição [0][0], ou seja, será printado [[2,2],[3,4]], {CONTINUAR}
"""