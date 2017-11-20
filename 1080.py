maior = 0
posicao = 0
for i in range(1, 101): # começa no 1 para mostrar corretamente a posição
    data = int(input())
    if data > maior:  # jeito "braçal", de pegar o maior número
        maior = data
        posicao = i  # Sempre que um "maior" cair aqui, a variável vai mudar
print(maior)
print(posicao)