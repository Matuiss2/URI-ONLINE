for i in range(100):
    numero = input()
    if float(numero) <= 10:  # pega os números <= a 10 com 1 casa decimal
        print("A[" + str(i) + "] =", format(float(numero), ".1f"))  # E imprime a posição dele na lista usando o i