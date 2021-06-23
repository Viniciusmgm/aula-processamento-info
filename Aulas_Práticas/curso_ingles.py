#Casos onde a categoria pode ser finalizada:
#- Acertar 2 faceis e 1 dificil
#- Acertar 2 dificeis
#- Acertar 1 facil e 1 desafio

"""    
Atividade:
- Completar o código feito em aula para que sejam apresentadas as perguntas da segunda categoria. Utilizar módulo.
- Quando o aluno passar para a 2a categoria ou o curso terminar, o programa deve parabenizá-lo caso ele tenha pulado alguma(s) pergunta(s). Isso deve ser feito utilizando-se no máximo 2 ifs.
"""

def ponto(teste):
  resp = input("Traduza " + teste[0] + ": ")
  if resp == teste[1]:
    return 1
  else:
    return 0 

#Função que utiliza os scores para dar parabéns
def parabens(fac_sc,dif_sc,des_sc):
  if((fac_sc == 2 and dif_sc == 1) or (fac_sc == 1 and des_sc == 1)or dif_sc == 2):
    print("\nParabéns por terminar essa fase pulando alguma pergunta!!\n")
  fac_sc = dif_sc = des_sc = 0
  return fac_sc, dif_sc, des_sc

#Função que executa a segunda fase
def prox_fase(fase_com,fac_sc, dif_sc, des_sc):
  print("\t\t|---------- Fase 2 ----------|\n")
  fac_sc += ponto(fase_com[0])
  fac_sc += ponto(fase_com[1])
  dif_sc += ponto(fase_com[2])

  if not(fac_sc == 2 and dif_sc == 1):
    dif_sc += ponto(fase_com[3])
    if not(dif_sc == 2 or (fac_sc == 2 and dif_sc == 1)):
      des_sc += ponto(fase_com[4])
      if not(fac_sc >= 1 and des_sc == 1):
        des_sc += ponto(fase_com[5])

  return fac_sc, dif_sc, des_sc
  
  
def main():
  cor_fac_1 = ("vermelho", "red")
  cor_fac_2 = ("verde", "green")
  cor_dif_1 = ("laranja", "orange")
  cor_dif_2 = ("marrom", "brown")
  cor_des_1 = ("violeta", "violet")
  cor_des_2 = ("cinza", "gray")

  com_fac_1 = ("pao", "bread")
  com_fac_2 = ("laranja", "orange")
  com_dif_1 = ("macarrão", "pasta")
  com_dif_2 = ("abacaxi", "pineapple")
  com_des_1 = ("ensopado", "stew")
  com_des_2 = ("torta de maçã", "apple pie")

  #Lista que auxilia na passagem dos parametros para a função prox_fase
  fase_com = [com_fac_1, com_fac_2, com_dif_1, com_dif_2, com_des_1, com_des_2]

  fac_sc = 0
  dif_sc = 0
  des_sc = 0

  print("\t\t|---------- Fase 1 ----------|\n")
  fac_sc += ponto(cor_fac_1)
  fac_sc += ponto(cor_fac_2)
  dif_sc += ponto(cor_dif_1)

  if not(fac_sc == 2 and dif_sc == 1):
    dif_sc += ponto(cor_dif_2)
    if not(dif_sc == 2 or (fac_sc == 2 and dif_sc == 1)):
      des_sc += ponto(cor_des_1)
      if not(fac_sc >= 1 and des_sc == 1):
        des_sc += ponto(cor_des_2)
  
  #Dando parabens e zerando os scores
  fac_sc, dif_sc, des_sc = parabens(fac_sc, dif_sc, des_sc)
  #Recebendo os scores da segunda fase
  fac_sc, dif_sc, des_sc = prox_fase(fase_com, fac_sc, dif_sc, des_sc)
  #Dando parabens, caso tenha pulado alguma pergunta
  parabens(fac_sc, dif_sc, des_sc)
  

main()