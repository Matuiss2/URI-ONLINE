dinheiro = int(input())
cem = dinheiro // 100
sobra = dinheiro % 100
cinquenta = sobra // 50
sobra = sobra % 50
vinte = sobra // 20
sobra = sobra % 20
dez = sobra // 10
sobra = sobra % 10
cinco = sobra // 5
sobra = sobra % 5
dois = sobra // 2
sobra = sobra % 2
um = sobra
print(dinheiro)
print(cem, "nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(um, "nota(s) de R$ 1,00")