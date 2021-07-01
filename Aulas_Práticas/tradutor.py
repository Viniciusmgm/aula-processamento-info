"""
Enunciado:
- Construir um tradutor
- Recebe uma frase do usuário e a retorna traduzida palavra a palavra (literalmente)
- Palavras não encontradas no dicionário devem ficar marcadas

Atividade:
- Se uma palavra nao for encontrada no dicionario, procurar uma semelhante (primeira e ultima letra iguais e mesmo tamanho)
"""
#retorna a palavra encontrada, o precedente desta palavra e o restante da format
def prox_palavra(frase):
  i = 0
  precedente = ""
  palavra = ""

  while i < len(frase) and not(frase[i].isalnum()):
    precedente += frase[i]
    i += 1

  while i < len(frase) and frase[i].isalnum():
    palavra += frase[i]
    i += 1

  return(precedente, palavra, frase[i:])

def traduz(palavra, dicionario):
  if palavra in dicionario.keys():
    return(dicionario[palavra])
  else:
    """
    O processo de procurar por uma palavra semelhante ocorre dentro do else, pois caso seja no início, pode ocorrer um erro se houver 2 palavras semelhantes no dicionário
    """
    #verifica se alguma key do dicionario possui a primeira e ultima letra iguais a da palavra, e se os tamanhos são iguais
    for key in dicionario.keys():
      if len(palavra) == len(key) and palavra[0] == key[0] and palavra[len(palavra) - 1] == key[len(key) - 1]:
        palavra = key
    if palavra in dicionario.keys():
      return(dicionario[palavra])
    else:
      return "<{}>".format(palavra)


def main():
  frase = input("Digite a frase:\n")
  #ser ou não ser, sir a questão
  dicionario = dict(a = "the", o = "the", não = "no", ser = "to be", questão = "question")

  traducao = ""
  while len(frase) > 0:
    precedente, palavra, frase = prox_palavra(frase)
    traducao += precedente + traduz(palavra, dicionario)
    
  print(traducao)

main()