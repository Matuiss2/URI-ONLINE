inicial, acao = list(map(int, input().split()))
for i in range(acao):
    data = input()
    if data == "fechou":
        inicial += 1
    else:
        inicial -= 1
print(inicial)