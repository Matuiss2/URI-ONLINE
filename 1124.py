def f(l1, l2, r1, r2):
# Processo
    dx = l1 - r1 - r2
    dy = l2 - r1 - r2
    if dx < 0 or dy < 0:
        return False  # Se a soma dos raios for maior que um dos lados retorna falso, elimina vários casos
    return dx * dx + dy * dy >= (r1 + r2) * (r1 + r2) and min(l1, l2) >= 2 * max(r1, r2)
    # Valor bool, se couber volta True se não couber volta False


def main():
    while True:
# Entrada
        data = input().split()  # recebe o valor e separa
        l1 = int(data[0])
        l2 = int(data[1])
        r1 = int(data[2])
        r2 = int(data[3])
        if not (l1 + l2 + r1 + r2) > 0:  # Se todos os valores forem 0, o programa fecha(seguindo as instruções)
            break
# Saída
        if f(l1, l2, r1, r2):  # Chama e retorna o valor da função anterior, se for True entra aqui e imprime S
            print("S")
        else:  # Se for False entra aqui
            print("N")
    return 0


main()  # Chama e retorna o valor da função main

