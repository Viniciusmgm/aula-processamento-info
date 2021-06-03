def autonomia(carga):
    if(carga <= 50000):
        return 18000, 19800
    elif(carga <= 200000):
        return 9000, 9900
    else:
        return 3000, 3300

carga = int(input())
auto = autonomia(carga)
ax = float(input())
ay = float(input())
bx = float(input())
by = float(input())
dist = (((bx - ax) ** 2) + ((by - ay) ** 2)) ** 0.5

print(round(dist,2))
if(auto[0] >= dist):
    print("SIM")
elif(auto[1] >= dist):
    print("TALVEZ")
else:
    print("NAO")