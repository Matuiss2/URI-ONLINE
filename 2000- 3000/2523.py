# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
while True:
    try:
        lampadas = input()  # Letras das lampadas
        inutil = int(input())  # valor descartado nesse método
        data = input().split()  # Posições da lampada
    except EOFError:
        break
    frase = ""
    for i in data:
        frase += lampadas[int(i) - 1]  # -1, porque o index começa a contar no 0
    print(frase)