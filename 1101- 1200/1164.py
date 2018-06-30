for i in range(int(input())):
    numero, total = int(input()), 0
    for divisores in range(1, numero):
        if numero % divisores == 0:
            total += divisores
    if total == numero:
        print(numero, "eh perfeito")
    else:
        print(numero, "nao eh perfeito")
