n1, n2, total = int(input()), int(input()), 0
maior, menor = max(n1, n2), min(n1, n2)
for i in range(menor, maior + 1):
    if i % 13:
        total += i
print(total)
