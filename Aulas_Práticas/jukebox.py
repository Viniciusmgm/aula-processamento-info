"""
Jukebox
– Adicionar música
– Listar músicas
– Escolher música
– Escolher aleatoriamente

Atividade
- Adicione uma funcionalidade que permita o usuário ver as 3 músicas mais tocadas
- Adicione uma restrição que determina que uma música só pode ser tocada se ela não foi uma das últimas 3 a serem tocadas
"""
import random
import numpy

def restricao(escolha, ordem_music):
  if not(escolha in ordem_music):
    ordem_music.append(escolha)
    return True
  else:
    ordem_music.append(escolha)
    pos1_escolha = ordem_music.index(escolha)
    pos2_escolha = ordem_music.index(escolha, pos1_escolha + 1)
    if not(pos2_escolha - pos1_escolha) <= 3:
      return True
    return False

def main():
  menu = '| 1 - Listar músicas \n| 2 - Escolher \n| 3 - Surpresa \n| 4 - Adicionar \n| 5 - Músicas mais tocadas \n| 0 - Sair\n Escolha uma das opções apresentadas: '
  titulos = ['Que pena - Jorge Ben Jor', 'Como nossos pais - Elis Regina', 'Firework - Katy perry', 'Amiga da minha mulher - Seu Jorge']
  musicas = ['Ela já não gosta mais de mim\nMas eu gosto dela mesmo assim', 'Minha dor é perceber\nQue apesar de termos', 'Do you ever feel like a plastic bag?', 'ela é amiga da minha mulher, pois é pois é']
  mais_tocadas = numpy.array([0] * len(titulos))
  ordem_music = list()

  opcao = input(menu)
  while(opcao != '0'):
    if opcao == '1':
      for i in range(len(titulos)):
        print("{}: {}".format(i + 1, titulos[i]))
    elif opcao == '2':
      escolha = int(input('Escolha pelo número: '))
      if restricao(escolha - 1, ordem_music) == True:
        print(musicas[escolha - 1])
        mais_tocadas[escolha - 1] += 1
      else:
        print("Infelizmente, você precisa esperar 3 músicas para tocar a que você escolheu")
    elif opcao == '3':
      escolha = random.randint(0,len(titulos) - 1)
      if restricao(escolha, ordem_music) == True:
        print(musicas[escolha])
        mais_tocadas[escolha] += 1
      else:
        print("Infelizmente, você precisa esperar 3 músicas para tocar a que você escolheu")
    elif opcao == '4':
      titulos.append(input('Digite o título e o artista: '))
      musicas.append(input('Digite um trechinho da música: '))
      mais_tocadas.append(0)
    elif opcao == '5':
      pos = mais_tocadas.argsort()
      print("As músicas mais tocadas foram: \n1 - {} \n2 - {} \n3 - {}".format(titulos[pos[len(pos) - 1]], titulos[pos[len(pos) - 2]], titulos[pos[len(pos) - 3]]))
    opcao = input("\n" + menu)

main()