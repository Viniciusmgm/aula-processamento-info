#Quantidade de notas no caixa
qtnnotas200 = 2
qtnnotas100 = 3
qtnnotas50 = 4
qtnnotas20 = 15
qtnnotas10 = 22
qtnnotas5 = 20

print("----- Bem Vindo ao Caixa -----")
print("Lembre-se que o máximo que pode-se sacar por vez é 1500 reais")
valor = int(input("Informe o valor que deseja retirar: "))

def calcNotas(cedula,quantia,qtndisp):
  x = min((quantia // cedula), qtndisp)
  restante = quantia - (cedula * x)
  return x, restante

notas200, valor = calcNotas(200,valor,qtnnotas200)
notas100, valor = calcNotas(100,valor,qtnnotas100)
notas50, valor = calcNotas(50,valor,qtnnotas50)
notas20, valor = calcNotas(20,valor,qtnnotas20)
notas10, valor = calcNotas(10,valor,qtnnotas10)
notas5, valor = calcNotas(5,valor,qtnnotas5)

'''
#Calcula qntas notas de 200
notas200 = min(qtnnotas200, (valor // 200))
valor = valor - (notas200 * 200)
#Calcula qntas notas de 100
notas100 = min(qtnnotas100, (valor // 100))
valor = valor - (notas100 * 100)
#Calcula qntas notas de 50
notas50 = min(qtnnotas50, (valor // 50))
valor = valor - (notas50 * 50)
#Calcula qntas notas de 20
notas20 = min(qtnnotas20, (valor // 20))
valor = valor - (notas20 * 20)
#Calcula qntas notas de 10
notas10 = min(qtnnotas10, (valor // 10))
valor = valor - (notas10 * 10)
#Calcula qntas notas de 5
notas5 = valor // 5
'''

print("Você receberá " + str(notas200) + " notas de 200" + "\n" + "Você receberá " + str(notas100) + " nota(s) de 100" + "\n" + "Você receberá " + str(notas50) + " nota(s) de 50" + "\n" + "Você receberá " + str(notas20) + " nota(s) de 20" + "\n" + "Você receberá " + str(notas10) + " nota(s) de 10" + "\n" + "Você receberá " + str(notas5) + " nota(s) de 5")