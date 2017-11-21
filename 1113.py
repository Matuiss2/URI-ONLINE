while True:
    data = input().split()
    if int(data[0]) == int(data[1]):  # Se forem valores iguais vai fechar o programa
        break
    elif int(data[0]) > int(data[1]):
        print("Decrescente")
    else:
        print("Crescente")