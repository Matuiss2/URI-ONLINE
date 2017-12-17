# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        data = input().split()
    except EOFError:
        break
    print(int(int(data[0]) * int(data[1]) * 2))