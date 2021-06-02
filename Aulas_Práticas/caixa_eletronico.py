valor = int(input("Informe o valor que deseja retirar: "))

#Calcula qntas notas de 200
notas200 = valor // 200
valor = valor - (notas200 * 200)
#Calcula qntas notas de 100
notas100 = valor // 100
valor = valor - (notas100 * 100)
#Calcula qntas notas de 50
notas50 = valor // 50
valor = valor - (notas50 * 50)
#Calcula qntas notas de 20
notas20 = valor // 20
valor = valor - (notas20 * 20)
#Calcula qntas notas de 10
notas10 = valor // 10
valor = valor - (notas10 * 10)
#Calcula qntas notas de 5
notas5 = valor // 5

print("Você receberá " + str(notas200) + " notas de 200" + "\n" + "Você receberá " + str(notas100) + " nota(s) de 100" + "\n" + "Você receberá " + str(notas50) + " nota(s) de 50" + "\n" + "Você receberá " + str(notas20) + " nota(s) de 20" + "\n" + "Você receberá " + str(notas10) + " nota(s) de 10" + "\n" + "Você receberá " + str(notas5) + " nota(s) de 5")