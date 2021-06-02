#Quantidade minima panqueca
panquecaFarinha = 100
panquecaPolvilho = 20
panquecaFermento = 10
#Quantidade minima pao
paoBatata = 300
paoPolvilho = 100
paoFermento = 10

farinha = int(input("Qual a quantidade de farinha na dispensa: "))  
polvilho = int(input("Qual a quantidade de polvilho na dispensa: "))  
fermento = int(input("Qual a quantidade de fermento na dispensa: "))  
batata = int(input("Qual a quantidade de batata na dispensa: ")) 

#Calcula a quantidade de vezes que conseguiria fazer panqueca
vezespanquecas = min((farinha // panquecaFarinha),(polvilho // panquecaPolvilho),(fermento // panquecaFermento))
#Calcula a quantidade de vezes que conseguiria fazer pao
vezespao = min((batata // paoBatata),(polvilho // paoPolvilho),(fermento // paoFermento))

print("Você conseguiria fazer a panqueca" + str(vezespanquecas) + "vezes")
print("Você conseguiria fazer a pao" + str(vezespao) + "vezes")
