roupas = int(input())
min_1, max_1 = map(int, input().split())  # Lavadora
min_2, max_2 = map(int, input().split())  # Secadora
if roupas in range(min_1, max_1 + 1) and roupas in range(min_2, max_2 + 1):  # +1 para incluir o próprio numero
    # Se couber nos dois é possível
    print("possivel")
else:
    print("impossivel")