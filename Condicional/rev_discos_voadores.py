ano = int(input())
cod_mot = int(input())
dist_luz = int(input())
if(ano >= 1901 and ano <= 2000):
    if(cod_mot == 100 or cod_mot == 101):
        print("SIM")
    else:
        print("NAO")
elif(ano >= 2001 and ano <= 2020):
    if(dist_luz > 5000):
        print("SIM")
    else:
        print("NAO")
elif(ano == 2021):
    if((cod_mot == 200 or cod_mot == 201) and dist_luz > 200):
        print("SIM")
    else:
        print("NAO")
else:
    print("NAO")