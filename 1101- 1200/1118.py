encerramento = 0
while encerramento != 2:
    corretas, total_notas = 0, 0
    while corretas < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            corretas += 1
            total_notas += nota
    print("media = {}".format(format(total_notas / 2, ".2f")))
    encerramento = int(input("novo calculo (1-sim 2-nao)\n"))
    while encerramento not in [1, 2]:
        encerramento = int(input("novo calculo (1-sim 2-nao)\n"))
