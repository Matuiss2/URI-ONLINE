# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
while True:
    n1 = float(input())
    while not 0 <= n1 <= 10:  # Validacao de input vai rodar ate chegar um valor valido(0 a 10)
        print("nota invalida")
        n1 = float(input())
    n2 = float(input())
    while not 0 <= n2 <= 10:
        print("nota invalida")
        n2 = float(input())
    print("media =", format((n1 + n2) / 2, ".2f"))
    break  # Quando os 2 valores forem corretos o programa vai fechar
