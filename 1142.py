# Não é uma maneira eficiente, pois faz número por número
numero = int(input())
p = 1  # O valor inicial sempre é 1
for i in range(numero):
    for j in range(p, p + 3):  # Vai pegar o valor p e iterar 3 vezes
        print(j, end=" ")  # Vai imprimir todos na mesma linha com um espaço usando end=
    print("PUM", end="")  # Vai adicionar na mesma linha essa str(tem que ser fora do loop j)
    print()  # Quebra a linha, terminando a concatenação do end=
    p += 4  # Aumenta o valor de p pelos 3 números já impressos e pula 1 como pede o exercício