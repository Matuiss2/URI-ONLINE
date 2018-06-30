for i in range(int(input())):
    numero = int(input())
    if numero in [0, 1]:
        print(numero, "nao eh primo")
        continue
    for divisores in range(2, numero // 2 + 1):
        if numero % divisores == 0:
            print(numero, "nao eh primo")
            break
    else:
        print(numero, "eh primo")
