# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        numero = int(input())
    except EOFError:
        break
    conta = 0
    double = 1  # Inicial é 1 pois é uma multiplicação
    if double == numero:  # Se já começa no número desejado não é necessaria nenhuma ação
        print(0)
    else:
        while double != numero:  # Quando chegar ao número desejado vai parar
            conta += 1  # Conta as ações
            double *= 2  # Dobra a cada iteração
        print(conta)