t = int(input())  # Pega o número de casos - teste
case = 1  # Apenas para apresentação
for i in range(t):  # Itera por uma quantidade de vezes determinada pelo input t
    numeros = input().split()  # Pega os casos - teste e os separa em números e tipo
    numero = numeros[0]  # Pega o número a ser convertido
    tipo = numeros[1]  # Pega o tipo do número a ser convertido
    print("Case " + str(case) + ":")  # Imprime qual é o case
    if tipo == "dec":  # Se o tipo for decimal entra aqui
        print("{:x} hex".format(int(numero)))  # Pega 1 n int e volta como str o val hex desse número decimal usando{:x}
        print("{:b} bin".format(int(numero)))  # Pega 1 n int e volta como str o val bin desse número decimal usando{:b}
        case += 1  # Quando terminar adiciona 1 apenas para apresentação
        print()  # Pula uma linha apenas para apresentação
    elif tipo == "bin":  # Se o tipo for binário entra aqui
        dec = int(numero, 2)  # Pega o numero binário e converte para decimal usando esse método
        print(dec, "dec")  # Imprime o valor decimal desse binário
        print("{:x} hex".format(dec)) # Pega 1 n int e volta o val hex desse num dec(convertido anteriormente)usando{:x}
        case += 1  # Quando terminar adiciona 1 apenas para apresentação
        print()  # Pula uma linha apenas para apresentação
    else:  # Se o tipo for hexadecimal entra aqui
        dec = int(numero, 16)   # Pega o numero hexadecimal e converte para decimal usando esse método
        print(dec, "dec")   # Imprime o valor decimal desse hexadecimal
        print("{:b} bin".format(dec))  # Pega 1 n int e volta o val bin desse n dec(convertido anteriormente)usando{:b}
        case += 1  # Quando terminar adiciona 1 apenas para apresentação
        print()  # Pula uma linha apenas para apresentação
