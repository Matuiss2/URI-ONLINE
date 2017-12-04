a = 0  # Esse valores tem que estar fora do loop, ou vão resetar a cada iteração
g = 0
d = 0
while True:
    data = int(input())
    while data not in range(1, 5):  # Validação de valor de input, vai ficar pedindo um valor até ele ser um aceitavel
        data = int(input())
    if data == 4:  # Se for 4 vai fechar o programa
        break
    elif data == 1:
        a += 1
    elif data == 2:
        g += 1
    else:
        d += 1
print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)
