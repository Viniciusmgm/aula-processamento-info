#Exercício 1
"""
Assim como em um string, é possível se acessar as posições em listas de caracteres, porém a lista possibilita a mudança de um valor ou caractere em uma posição especifíca, já as strings possuem uma sequência ordenada imutável
"""

#Exercício 2
"""
Tanto o vencimentos, quanto o vencimentos_novo serão impressos como: [5, 15, 10]
Isso ocorre, pois nesse caso é necessário usar a função .copy() das listas para o vetor vencimentos e vencimentos_novo terem resultados diferentes, isso se deve ao fato das listas serem diferentes as variáveis comuns, logo, nesse trecho de código o que está sendo copiado, é o endereço do vetor original.
"""

#Exercício 3
"""
Os arrays do numpy são mais eficientes do que as listas no python, pois utilizam um quantidade menor de memória, assim como a biblioteca numpy possibilita algumas funcionalidades a mais.
"""

#Exercício 4
"""
def vezes_palavra(texto, palavra):
  texto = texto.split(" ")
  num_vezes = texto.count(palavra)
  print("A palavra {} aparece no texto {} vezes".format(palavra, num_vezes))

vezes_palavra("só sei que nada sei", "sei")
"""