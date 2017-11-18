loops = int(input())  # Não deve ser o método mais eficiente, mas é bom mesmo assim
for i in range(loops):
    data = input()
    num_str = ""
    for j in data:
        if j.isdigit():
            num_str += j  # Manda os números como strings para a variável
        else:
            num_str += " "  # Transforma as letras em espaços, eu incluí para separar os números
    print(sum(map(int, num_str.split())))
    '''
    split(), separa os números pelos espaços, e os tranforma em itens de uma lista
    map(int, lista), transforma todas as strings em números inteiros ex: "123" --- 123
    sum(lista), soma todos os valores (se forem int) de uma lista
    ''' 