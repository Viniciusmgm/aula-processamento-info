def planeta(num):
  if(num == 80):
    return "Marte"
  elif(num == 81):
    return "Saturno"
  elif(num == 90):
    return "Netuno"
  else:
    return "HD21749b"

def modelo(num):
  if(num == 60):
    return "A6000"
  elif(num == 61):
    return "B7500"
  else:
    return "C9000"

num = str(input())
lista = list(num)
print(planeta(int(lista[0]+lista[1])))
print(planeta(int(lista[2]+lista[3])))
print(modelo(int(lista[4]+lista[5])))