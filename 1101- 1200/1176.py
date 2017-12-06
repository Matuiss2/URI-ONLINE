def fib(n, d):
    a, b = 0, 1
    fibo = [0]
    for j in range(n):
        a, b = b, a + b
        fibo.append(a)
    return fibo[d]  # pega o valor da posição requerida do input na lista de fibonacci


loops = int(input())  # Vê a qntd de casos testes
for i in range(loops):
    data = int(input())
    print("Fib(" + str(data) + ") = " + str(fib(60, data)))  # transformei em str, para formatar o print + facilmente
