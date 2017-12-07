# É a lista da fib, so que em de ser só soma, intercala soma e multiplicação
def fib(n):
    list_phil = [0, 1]
    a, b = 0, 1
    for i in range(n - 1):
        if i % 2 == 0:  # Intercala entre + e *
            a, b = b, a + b
        else:
            a, b = b, a * b
        list_phil.append(a)
    return list_phil[-1]  # Retorna o último valor


while True:
    try:
        data = int(input())
    except EOFError:
        break
    # Se não tivesse isso daria errado qnd data fosse 1, pois a lista inicial da função começa com 2 valores
    if data == 1:
        print(0)
    else:
        print(fib(data))
