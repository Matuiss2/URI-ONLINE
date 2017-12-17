con = 'n'
while con == 'n':
    cont, media, a = 0, 0, 3
    while cont < 2:
        X = float(input())
        if 0 <= X <= 10:
            cont += 1
            media += X
        else:
            print("nota invalida")
    print('media =', format(media / 2, ".2f"))
    while a not in [1, 2]:
        a = int(input("novo calculo (1-sim 2-nao)\n"))
        if a == 1:
            con = 'n'
        elif a == 2:
            con = 's'
        else:
            a = int(input("novo calculo (1-sim 2-nao)\n"))