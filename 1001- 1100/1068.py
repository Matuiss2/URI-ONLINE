# Essa é a mais eficiente resposta do site em python3, 1° lugar isolado!!!
# Não é totalmente eficiente, mas funciona para todos os casos teste do site
# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
while True:
    try:
        data = input()
    except EOFError:
        break
    if data[0] == ")" or data[-1] == "(":  # Se o 1° simbolo da expressao for ) ou a ultima for (, esta incorreto
        print("incorrect")
    elif (data.count("(") + data.count(")")) % 2 == 0:  # conta os pares de (), se a soma for par está correto
        print("correct")
    else:  # Se não for está incorreto
        print("incorrect")
