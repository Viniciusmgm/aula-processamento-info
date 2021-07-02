def primo(num):
    for val in range(2,num):
        if num % val == 0:
            return False
    return True

def main():
  n = int(input())
  aux = range(2,n*n)
  j = 0
  for i in aux:
    if primo(i) == True and j < n:
      j += 1
      print(i)

main()