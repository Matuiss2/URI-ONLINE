# Outro método seria incluir todas os números numa lista, e imprimir max(lista) + 1
maior = 0  # só funciona com 0 porque todos os números são positivos
while True:
    try:
        numero = int(input())
    except EOFError:
        break
    if numero > maior:  # Sempre que vier um número maior vai mudar a variavel
        maior = numero
    else:
        break
print(maior + 1)