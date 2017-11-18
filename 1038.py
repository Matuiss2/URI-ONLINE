codigo = input().split()
item = int(codigo[0])
qnt = int(codigo[1])
if item == 1:
    total = qnt * 4.00
elif item == 2:
    total = qnt * 4.50
elif item == 3:
    total = qnt * 5.00
elif item == 4:
    total = qnt * 2.00
else:
    total = qnt * 1.50
print("Total: R$", format(total, ".2f"))
