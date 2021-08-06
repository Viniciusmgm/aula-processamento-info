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
def porc(M, idade, temp_entrega):
  soma = 0
  for i in range(len(M)):
    if(M[i][2] > idade and M[i][4] < temp_entrega):
      soma += 1
  return (soma / len(M)) * 100

def main():
  M = [[3000, 2, 25, 20, 40], [4500, 3, 30, 10, 30], [2000, 4, 41, 20, 20], [4800, 8, 60, 20, 25], [8000, 15, 70, 30, 60]] 
  idade = 40
  temp_entrega = 30
  print("{} % dos funcionários tem idade maior que {} anos, e possuem uma média de tempo de entrega de projeto menor que {} horas".format(porc(M, idade, temp_entrega), idade, temp_entrega))

main()
"""

#Exercício 3
"""
O n1 vai ser printado como 5, já a matriz terá um acréscimo na posição [0][0], ou seja, será printado [[2,2],[3,4]]. Isso ocorre, pois a variável é modificada localmente na função, não alterando o seu valor real. Já o comportamento da matriz, se deve ao fato dela nã ser nada mais do que uma lista de listas, e sendo assim, como o que é copiado é o endereço dessa lista, então, o valor guardado no seguinte endereço é alterado, alterando assim, a lista original.
"""