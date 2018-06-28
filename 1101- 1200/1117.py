corretas, total_notas = 0, 0
while corretas < 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        corretas += 1
        total_notas += nota
print("media =", format(total_notas / 2, ".2f"))
