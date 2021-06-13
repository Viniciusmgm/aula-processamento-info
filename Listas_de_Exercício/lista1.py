#Lista 1

#Exercício 1
#a)Algoritmo:
"""
Entrada: posições de x e y da flecha
Saída: posição da flecha no alvo 
inicio (dentro do método main())
  recebe posição x
  recebe posição y
  calcula a distãncia entre (x,y) e a origem
  criação do método posição
  chamada do método posição
    se a distância for menor que ou igual a 1
      retorna que está na região A
    se a distância for menor que ou igual a 2
      retorna que está na região B
    se a distância for menor que ou igual a 3
      retorna que está na região C
    se a distância for menor que ou igual a 4
      retorna que está na região D
    se a distância for menor que ou igual a 5
      retorna que está na região E
    senão
      retorna que está fora do alvo
  fim do método posição
  imprime região na tela
fim
"""

#b)Código em Python:
"""
def posicao(dist):
  if(dist <= 1):
    return "A flecha atingiu a região A"
  elif(dist <= 2):
    return "A flecha atingiu a região B"
  elif(dist <= 3):
    return "A flecha atingiu a região C"
  elif(dist <= 4):
    return "A flecha atingiu a região D"
  elif(dist <= 5):
    return "A flecha atingiu a região E"
  else:
    return "A flecha foi para fora do alvo"

def main():
  x = float(input("Qual a posição x da flecha? "))
  y = float(input("Qual a posição y da flecha? "))
  dist = ((x - 0)) + ((y ** 2)) ** 0.5
  print(posicao(dist))
main()
"""

#Exercício 2
"""
O simbolo de igual(=) é usado para atribuição de um valor a uma variável. Já o simbolo de igualdade(==) é
utilizado para fazer a comparação entre 2 valores, ou variáveis

Exemplos:
a) Simbolo de = :
valor = 8
print(valor) #imprime o número 8, que foi atribuido a variável valor

b) Simbolo de == :
valor1 = 5
valor2 = 6
print(valor1 == valor2) #Imprime o valor booleano False, pois o valor1 que é 5, não é igual ao valor2 que é 6
"""

#Exercício 3
"""
a)
b)
"""

#Exercício 4
"""
O return é usado para retornar um valor da função, assim como pode ser usado para finalizar a execução de uma função
"""

#Exercício 5
"""
a) Não há conversão do tipo da entrada, ou seja, o input irá armazenar uma string, logo, é necessário fazer a conversão de string para int. 
Após realizar a conversão, é necessário converter novamente em string para poder concatenar a variável na hora de printar 

b) Código resolvido:
valor_dolar = 5.07
x_dolares = int(input("Quantas dólares você quer comprar? "))
print("Você precisa de " + str(valor_dolar * x_dolares) + " reais")
"""


