notas = input().split()  # separa os dados de uma mesma linha
n1 = float(notas[0]) * 2
n2 = float(notas[1]) * 3
n3 = float(notas[2]) * 4
n4 = float(notas[3])
media = (n1 + n2 + n3 + n4) / 10
print("Media:", format(media, ".1f"))
if media >= 7:
    print("Aluno aprovado.")
elif 5 <= media < 7:
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame:", format(ne, ".1f"))
    if (ne + media) / 2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:", format((ne + media) / 2, ".1f"))
else:
    print("Aluno reprovado.")