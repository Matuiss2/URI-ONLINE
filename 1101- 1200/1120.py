while True:
    data = input().split()
    errado = data[0]
    numero = data[1]
    if int(errado) + int(numero) == 0:  # Condição de parada do loop
        break
    novo_numero = numero.replace(errado, "")  # substitui o errado por um vazio
    if novo_numero == "":  # Se não sobrar nada entra aqui, se não tivesso isso daria erro na conversão para int
        print(0)
    else:
        print(int(novo_numero))  # Converte para int, para dar o output esperado
