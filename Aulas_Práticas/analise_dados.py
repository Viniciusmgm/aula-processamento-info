"""
Analises
- Dados (https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/)
- Grafico
- Media movel
- Normalizacao de amplitude e translacao
- Discretizacao

Atividade
- Comparacao
"""

import matplotlib.pyplot as plt

def dissimilaridade(serie_temp1, serie_temp2, janela):
  serie_temp1 = norm_amplitude(serie_temp1)
  serie_temp1 = norm_translacao(serie_temp1)
  serie_temp1 = discretiza(serie_temp1, janela)
  serie_temp2 = norm_amplitude(serie_temp2)
  serie_temp2 = norm_translacao(serie_temp2)
  serie_temp2 = discretiza(serie_temp2, janela)
  dissim = "formula aqui"
  print("A dissimilaridade entre as séries é {}".format(dissim))


def suavizar(serie, janela):
  nova = serie.copy()
  for i in range(janela, len(serie)):
    nova[i] = sum(serie[(i - janela):i]) / janela
  return nova

def norm_amplitude(serie):
  import statistics as stat
  nova = list()
  dp = stat.stdev(serie)
  for i in serie:
    nova.append(i / dp)
  return nova

def norm_translacao(serie):
  nova = list()
  media = sum(serie) / len(serie)
  for i in serie:
    nova.append(i - media)
  return nova

def plota_salva(serie, nome):
  plt.plot(serie)
  plt.savefig(nome)
  plt.clf()

def discretiza(serie, janela):
  import math
  nova = list()
  for i in range(math.floor(len(serie) / janela)):
    fatia = serie[(i * janela) : (i * janela + janela)]
    media_fatia = sum(fatia) / janela
    nova.extend([media_fatia] * janela)
  return nova

def main():
  #numeros de novos casos de covid-19 no primeiros 61 dias a partir do primeiro caso nas cidades Santo André, São Paulo e São Bernardo do Campo   
  SA = [1,0,1,0,1,0,0,0,0,7,6,1,0,0,23,8,3,8,11,1,1,2,24,15,17,9,3,5,3,10,26,19,17,14,11,10,13,5,11,10,43,5,34,42,48,51,46,13,2,6,38,135,44,33,48,41,4,35,84,104,72]
  SP = [1,0,0,0,0,1,3,0,6,3,0,3,11,15,0,18,0,83,11,58,45,47,0,0,0,0,416,177,145,0,0,189,652,533,397,387,294,116,142,504,689,530,505,149,221,66,287,1059,144,836,684,240,147,527,349,534,575,1298,415,476,1408]
  SBC = [1,0,2,0,1,0,0,0,0,9,0,2,0,0,18,11,8,7,11,7,4,8,40,18,17,4,4,7,6,16,30,24,26,13,3,1,12,29,19,63,42,12,36,55,50,66,23,15,11,12,82,80,39,73,63,15,4,23,88,111,63]

  #plt.plot(SA)
  ##plt.show()
  ##plt.savefig('original')
  #plt.savefig('original.jpg', format = 'jpg')
  #plt.clf()

  #plota_salva(suavizar(SA, 3), 'suave5')

  #plota_salva(suavizar(SA, 7), 'suave7')

  #plota_salva(norm_amplitude(SA), 'norm_amp')

  #plota_salva(norm_amplitude(SA), 'norm_amp')

  #plota_salva(norm_translacao(SA), 'norm_translacao')

  #plota_salva(discretiza(SA, 5), 'discretiza')

  janela = int(input("Qual a janela você deseja? "))
  dissimilaridade(SA, SP, janela)

main()