soma_media = input()
total = 0
fora = 10
dentro = 1
numeros = 0
flag = False
inicial_fora = fora
inicial_dentro = dentro
for i in range(144):
    data = float(input())
    if i < 23:
        continue
    if flag is False:
        if inicial_fora + inicial_dentro == 0:
            fora -= 1
            dentro += 1
            inicial_fora = fora
            inicial_dentro = dentro
        if inicial_dentro > 0:
            if inicial_dentro == 5:
                flag = True
                fora = 7
                dentro = 5
                inicial_fora = fora
            inicial_dentro -= 1
            total += data
            numeros += 1
            continue
        if inicial_fora > 0:
            inicial_fora -= 1
            continue
    else:
        if inicial_fora + inicial_dentro == 0:
            fora += 1
            dentro -= 1
            if i == 79:
                dentro = 5
            inicial_fora = fora
            inicial_dentro = dentro
        if inicial_dentro > 0:
            inicial_dentro -= 1
            total += data
            numeros += 1
            continue
        if inicial_fora > 0:
            inicial_fora -= 1
            continue

if soma_media == 'S':
    print(format(total, ".1f"))
else:
    print(format((total / numeros), ".1f"))