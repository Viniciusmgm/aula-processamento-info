#Biblioteca
#Módulos: adicionar livros, retirar livros, apresentar livros, ranking melhores livros, pesquisa por categoria, sugestão aleatória
import random

def imprimir(estante, pos): #Imprime os dados do livro
  print("=======================================")
  print("Nome: {} ".format(estante[pos][0]))
  print("Categoria: {}".format(estante[pos][1]))
  print("Nota: {}".format(estante[pos][2]))

def apresentar(estante): #Apresenta os livros da estante
  for i in range(len(estante)): #percorre a estante
    imprimir(estante, i)

def adicionar(estante): # Adiciona o livro na estante conforme o nome, categoria do livro e a nota dada por quem adicionou.
  nome = input("Digite o nome do livro: ")
  categoria = input("Digite sua categoria: ")
  nota = input("Digite a nota: ")
  livro = [nome, categoria, nota]
  estante.append(livro) #adiciona a linha formada pelo nome, categoria e nota na matriz
  return estante #retorna a matriz

def retirar(estante): #Retira o livro da estante
  nome = input("Digite o nome do livro que deseja retirar: ")
  for i in range(len(estante)-1):   #percorrer as linhas da matriz
    if nome in estante[i]:
      estante.remove(estante[i])  #remover a linha da matriz, na posição indicada pelo nome inserido

def sugestao(estante):
  num = random.randint(0, len(estante)-1)  #gera uma posição de linha aleatória da matriz
  imprimir(estante, num)
  retirar = input("Você aceita a sugestão?(s/n) ")
  if retirar == "s":
    estante.remove(estante[num])  #o usuário remove o livro da sugestão, caso ele aceite-a, para ler.

def pesquisa(estante):
  categoria = input("Digite a categoria desejada: ")
  for i in range(len(estante)):   #percorrer as linhas da matriz
    if categoria in estante[i]: #Verifica se o livro, no caso a linha, possui a determinda categoria, e depois imprime os livros que possuem
       imprimir(estante, i)

def ranking(estante):
  for i in range(len(estante)): #percorre as linhas da matriz
    for j in range(i, len(estante)): #percorre as linhas de i até o final da matriz
      if estante[i][2] < estante[j][2]: #comparação da nota da posição i com as notas das seguintes posições, denotadas por j
        estante[i], estante[j] = estante[j], estante[i] #troca a posição das linhas
  apresentar(estante) #imprimir a matriz com o novo ranqueamento

def main():
  #Matriz com os livros
  estante = [["Harry Potter e a Pedra Filosofal", "Fantasia", 5.0], ["A Culpa é das Estrelas", "Romance", 4.0], ["Percy Jackson e o Ladrão de Raios", "Aventura", 4.5], ["Revolução dos Bichos", "Ficção", 4.7], ["Senhor dos Anéis", "Fantasia", 3.0], ["Capitão América: Guerra Civil", "Heróis", 5.0]]

  opcao = input("| 1- Apresentar Livros \n| 2- Adicionar Livros \n| 3- Retirar Livros \n| 4- Sugestão Aleatória de Livro \n| 5- Pesquisa por Categoria \n| 6- Ranking dos Livros \n| 0- Sair da Conta \nQual das opções deseja executar? ")
  #Apresenta as opções ao usuário
  while opcao != "0":
    if opcao == "1":
      apresentar(estante)
    elif opcao == "2":
      estante = adicionar(estante)
    elif opcao == "3":
      retirar(estante)
    elif opcao == "4":
      sugestao(estante)
    elif opcao == "5":
      pesquisa(estante)
    elif opcao == "6":# Os ranques vão de zero a cinco.
      ranking(estante)
    # Ao final de cada escolha e sua execução, volta ao menu de escolhas.  
    opcao = input("\n| 1- Apresentar Livros \n| 2- Adicionar Livros \n| 3- Retirar Livros \n| 4- Sugestão Aleatória de Livro \n| 5- Pesquisa por Categoria \n| 6- Ranking dos Livros \n| 0- Sair da Conta \nQual das opções deseja executar? ")

main()