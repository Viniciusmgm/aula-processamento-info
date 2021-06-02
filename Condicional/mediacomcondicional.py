def media(nota1,nota2):
    med = (nota1 + nota2) / 2
    return med

nota1 = int(input())
nota2 = int(input())
print(f'{media(nota1,nota2):.02f}')
if(media(nota1,nota2) >= 5):
    print("APROVADO")
else:
    rec = int(input())
    print(f'{media(media(nota1,nota2),rec):.02f}')
    if(media(media(nota1,nota2),rec) >= 5):
        print("APROVADO")
    else: 
        print("REPROVADO")