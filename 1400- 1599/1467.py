# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        data = input()
    except EOFError:
        break
    for i in data:
        if data.count(i) == 1:  # acha o valor isolado usando método de exaustão (pouco eficiente)
            if data.index(i) == 0:  # confere a posição do valor isolado
                print("A")
                break
            elif data.index(i) == 2:
                print("B")
                break
            else:
                print("C")
                break
    else:  # Se forem todos iguais não vai quebrar o loop anterior e vai entrar aqui(método só possível em python)
        print("*")