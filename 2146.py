# Smp q tiver 1 exercício q diz q o último valor é umarquivo final ou valor EOF use esse método
while True:
    try:
        data = int(input())
    except EOFError:
        break
    print(data - 1)  # A fórmula é o valor - 1
