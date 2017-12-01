dia = int(input())
anos = dia // 365
resto_a = dia % 365
meses = resto_a // 30
resto_m = resto_a % 30
dias = resto_m // 1
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
