# Smp q tiver 1 exercício q diz q o último valor é valor vazio(n confundir com 0 ou "") ou valor EOF use esse método
while True:
    try:
        tamanho = int(input())  # Valor inútil usando esse método
        data = input().split()  # Separa as velocidades em itens de uma lista(eles serão em str)
    except EOFError:
        break
    maior = max(map(int, data))  # Tranforma os valores da lista em int usando map, e pega o maior usando o max
    if maior < 10:
        print(1)
    elif maior in range(10, 20):
        print(2)
    else:
        print(3)