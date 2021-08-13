"""
Rede social:
- Adiciona usuário
- Adiciona amizade
- Mostra número e lista de amigos

Atividade:
- Adicionar uma funcionalidade que calcule o número de amigos em comum entre 2 usuários e mostre os nomes
"""
def imprime_matriz_rotulos(M):
    nlin = len(M)
    ncol = len(M[0])
    
    print(' ', end = ' ')
    for i in range(ncol):
        print(i, end = ' ')
    print()
        
    for i in range(nlin):
        print(i, end = ' ')
        for j in M[i]:
            print(j, end = ' ')
        print()

def aumenta_matriz(mat):
  if len(mat) == 0:
    mat.append([0])
  else:
    for i in mat:
      i.append(0)
    mat.append([0] * len(mat[0]))
  
def main():
  amizades = list()
  usuarios = list()
  menu = '|1- Adicionar usuário \n|2- Adicionar amizade \n|3- Mostrar número e lista de amigos \n|4- Listar usuários \n|5- Amigos em comum entre 2 usuários \n|0-Sair \nDeseja executar qual das opções? '

  opcao = input(menu)
  while opcao != '0':
    if opcao == '1':
      nome = input('Qual o seu nome? ')
      usuarios.append(nome)
      aumenta_matriz(amizades)
    elif opcao == '2':
      pessoa1 = int(input('Qual é o id da pessoa 1? '))
      pessoa2 = int(input('Qual é o id da pessoa 2? '))
      amizades[pessoa1][pessoa2] = 1
      amizades[pessoa2][pessoa1] = 1
    elif opcao == '3':
      pessoa = int(input('Qual o id da pessoa? '))  
      print('Voce tem {} amigos'.format(sum(amizades[pessoa])))
      for i in range(len(amizades)):
        if amizades[pessoa][i] == 1:
          print(usuarios[i])
    elif opcao == '4':
      for i in range(len(usuarios)):
        print('{}: {}'.format(i, usuarios[i]))
    elif opcao == '5':
      pessoa1 = int(input('Qual é o id da pessoa 1? '))
      pessoa2 = int(input('Qual é o id da pessoa 2? '))
      amigos_comum = 0
      print("Amigo(s) em comum:")
      for i in range(len(amizades)):
        if amizades[pessoa1][i] == 1 and amizades[pessoa2][i] == 1:
          amigos_comum += 1
          print(usuarios[i])
      print("No total, os usuários informados possuem {} amigo(s) em comum".format(amigos_comum))
    opcao = input("\n" + menu)

main()