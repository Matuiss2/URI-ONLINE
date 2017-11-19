loops = int(input())
dentro = 0
fora = 0
for i in range(loops):
    data = int(input())
    if data in range(10, 21):
        dentro += 1
    else:
        fora += 1
print(dentro, "in")
print(fora, "out")