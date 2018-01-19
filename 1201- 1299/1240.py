for i in range(int(input())):
    a, b = input().split()
    if len(b) > len(a):  # se for maior não encaixa isso elimina rapidamente vários casos
        print("nao encaixa")
    # se o final do "numero" a for igual a b encaixa
    elif b == a[-len(b):]:  # a[-len(b):], pega o final da string a seguindo o tamanho da string b
        print("encaixa")
    else:
        print("nao encaixa")