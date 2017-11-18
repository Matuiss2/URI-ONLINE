while True:
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    if m + n == 0:
        break  # Se os 2 forem 0 fecha o programa
    total = str(m + n).replace("0", "")  # Todos os 0 depois da soma serão removidos
    print(total)


