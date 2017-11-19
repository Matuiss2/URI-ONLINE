positivos = 0
t_data = 0
for i in range(6):
    data = float(input())
    if data >= 0:
        positivos += 1
        t_data += data
print(positivos, "valores positivos")
print(format(t_data / positivos, ".1f")) 