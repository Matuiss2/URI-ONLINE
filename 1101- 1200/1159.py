while True:
    numero = int(input())
    if numero == 0:
        break
    if numero % 2:
        print((numero + 1) * 5 + 20)
    else:
        print(numero * 5 + 20)
