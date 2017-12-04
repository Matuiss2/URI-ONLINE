loops = int(input())
for i in range(loops):
    data = input().split()
    menor = min(map(int,data))  # map converte as (str) para (int), min pega o menor valor(o inicial para o for)
    maior = max(map(int,data))  # map converte as (str) para (int), min pega o maior valor(o final para o for)
    total_i = 0
    for j in range(menor + 1, maior):  # + 1 pois não pode incluir o próprio número
        if j % 2 != 0:
            total_i += j  # Acumula todos os ímpares
    print(total_i)
