# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
while True:
    try:
        data = int(input())
    except EOFError:
        break
    if data == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")    
