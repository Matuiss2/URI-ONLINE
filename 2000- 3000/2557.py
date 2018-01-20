while True:
    try:
        data = input().replace("=", "+").split("+")  # Remove os símbolos
    except EOFError:
        break
    numeros = []
    for i in data:
        if i.isdigit():
            numeros.append(i)
    if data[-1] == "J":
        print(int(numeros[0]) + int(numeros[1]))
    else:
        print(int(numeros[1]) - int(numeros[0]))