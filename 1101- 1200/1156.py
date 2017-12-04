s = 0
div = 1
for i in range(1, 40, 2):  # o i vai de 1 a 39 pulando 2 a 2
    s += i / div
    div *= 2  # O divisor dobra a cada etapa
print(format(s, ".2f"))
