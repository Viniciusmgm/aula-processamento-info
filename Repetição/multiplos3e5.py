def mult_3e5(n, mult):
    if n % 3 == 0:
        mult["mult_3"] += 1
    if n % 5 == 0:
        mult["mult_5"] += 1
    return mult

def main():
    mult = dict(mult_3 = 0, mult_5 = 0)
    n = 1
    while n != 0:
        mult = mult_3e5(n, mult)
        n = int(input())
        
    print(mult["mult_3"])
    print(mult["mult_5"])
main()