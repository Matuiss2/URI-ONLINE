loops = int(input())
for i in range(loops):
    numero = int(input())
    if numero in range(0, 2):
        print(numero, "nao eh primo")  # 0 e 1 não são primos
    else:
        for j in range(2, numero):  # excluí o próprio número e o 1
            if numero % j == 0:
                print(numero, "nao eh primo")
                break
        else:  # se não for quebrado pelo break vai entrar aqui
            print(numero, "eh primo")
