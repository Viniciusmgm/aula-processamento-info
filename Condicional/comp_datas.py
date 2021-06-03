def comp(data1,data2):
    if(data1[0] < data2[0]):
        return "DATA1"
    elif(data1[0] == data2[0]):
        if(data1[1] < data2[1]):
            return "DATA1"
        elif(data1[1] == data2[1]):
            if(data1[2] < data2[2]):
                return "DATA1"
            elif(data1[2] == data2[2]):
                return "IGUAIS"
            else:
                return "DATA2"
        else:
            return "DATA2"
    else:
        return "DATA2"

dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())
data1 = ano1, mes1, dia1
data2 = ano2, mes2, dia2
print(comp(data1,data2))