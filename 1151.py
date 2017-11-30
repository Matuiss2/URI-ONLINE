def fib(n):
    a, b = 0, 1
    print(a, end=" ")
    f = ""
    for i in range(n - 1):  # -1 pois o 0 ja foi impresso
        a, b = b, a + b
        f += str(a) + " "
    return f[:-1]  # Exclui o ultimo espaco para nao dar presentation error


data = int(input())
print(fib(data))