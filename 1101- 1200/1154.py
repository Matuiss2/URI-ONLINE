idade, total, qntd = int(input()), 0, 0
while idade > 0:
    total += idade
    qntd += 1
    idade = int(input())
print(format(total / qntd, ".2f"))
