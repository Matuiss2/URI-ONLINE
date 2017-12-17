loops = int(input())
for i in range(loops):
    data = input()
    metade = len(data) // 2
    print((data[:metade][::-1]) + (data[metade:][::-1]))
# Pega a metade da frase e inverte cada uma delas mantendo a mesma ordem