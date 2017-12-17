data = input().split()
a = int(data[0])
loops = 0
for j in (data[1:]):
    if int(j) > 0:
        loops = int(j)
        break
soma = 0
for i in range(loops):
    soma += a + i
print(soma)
