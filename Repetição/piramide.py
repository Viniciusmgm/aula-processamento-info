def piramid(n):
    n_hifen = n
    for i in range(n):
        n_hifen -= 1
        print("-" * n_hifen, end = "")
        print("1" * ((i * 2) + 1), end = "")
        print("-" * n_hifen)

def main():
    n = int(input())
    piramid(n)
    
main()