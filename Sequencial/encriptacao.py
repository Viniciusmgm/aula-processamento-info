num = input()
encrip = list(num)
i = 0
encriptado = ''
while i != len(encrip):
    aux = int(encrip[i])
    if (aux < 9):
        aux += 1
        encrip[i] = str(aux)
    else:
        encrip[i] = "0"
    i += 1
for x in encrip:
    encriptado += x
print(encriptado)