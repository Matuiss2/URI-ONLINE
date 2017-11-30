# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
while True:
    data = input().split()
    if int(data[0]) == 0 or int(data[1]) == 0:  # se qq  valor for 0 vai fechar o programa
        break
    if int(data[0]) > 0:
        if int(data[1]) > 0:
            print("primeiro")
        else:
            print("quarto")
    else:
        if int(data[1]) > 0:
            print("segundo")
        else:
            print("terceiro")