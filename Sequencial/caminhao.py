capac = int(input())
qtn500 = capac // 500
capac = capac - (qtn500 * 500)
qtn100 = capac // 100
capac = capac - (qtn100 * 100)
qtn25 = capac // 25
capac = capac - (qtn25 * 25)
print(qtn500)
print(qtn100)
print(qtn25)
print(capac)