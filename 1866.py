loops = int(input()) # Vê a qntd de casos testes
for i in range(loops):
    numero = int(input())
    if numero % 2 == 0:  # Não precisa fazer uma iteração imensa, se for par é 0 se for ímpar é 1
        print(0)
    else:
        print(1)