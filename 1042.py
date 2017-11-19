data = input().split()  # Separa os números e pões em uma lista
for i in sorted(map(int, data)):  # Transforma os números em int usando map(), e pões em ordem usando sorted()
    print(i)
print()
for j in data:
    print(j)  # Não é necessário converter para int aqui