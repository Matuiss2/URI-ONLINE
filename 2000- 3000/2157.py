loops = int(input())
for i in range(loops):
    data = input().split()
    final = ""
    for j in range(int(data[0]), int(data[1]) + 1):  # +1 para incluir o próprio número, o mesmo no for: da linha 7
        final += str(j)
    for k in range(int(data[1]), int(data[0]) - 1, - 1):
        final += str(k)[::-1]  # Imprime invertido e na ordem decrescente para fazer uma string espelhada
    print(final)