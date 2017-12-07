# Smp q tiver 1 exercício q diz q o último valor é um arquivo final ou valor EOF use esse método
c_vit = {"suco": 120, "morango": 85, "mamao": 85, "goiaba": 70, "manga": 56, "laranja": 50, "brocolis": 34}
while True:
    loops = int(input())
    if loops == 0:
        break
    total = 0
    for i in range(loops):  # Vê a qntd de casos testes
        data = input().split()
        # Vê o nome e retorna o valor corrrespondente no dicionário, depois multiplica esse valor pela qnt
        total += c_vit[data[1]] * int(data[0])
    if total in range(110, 131):
        print(total, "mg")
    elif total in range(0, 110):
        print("Mais", 110 - total, "mg")
    else:
        print("Menos", total - 130, "mg")
