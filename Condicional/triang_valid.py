def triang(lado1,lado2,lado3):
    if(lado1 > (lado2 + lado3)):
        return "INVALIDO"
    elif(lado2 > (lado1 + lado3)):
        return "INVALIDO"
    elif(lado3 > (lado2 + lado1)):
        return "INVALIDO"
    else:
        return "VALIDO"
        
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
print(triang(lado1,lado2,lado3))