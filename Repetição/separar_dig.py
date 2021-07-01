def inverte(n):
    nova_string = ""
    n.split()
    i = len(n) - 1
    while i >= 0:
        nova_string += n[i]
        i -= 1
    return nova_string
    

def main():
    n = input()
    n = inverte(n)
    for i in n:
        print(i)
    
main()