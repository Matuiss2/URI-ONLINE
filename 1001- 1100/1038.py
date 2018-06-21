codigo, quantidade = map(int, input().split())
tabela_precos = [4, 4.5, 5, 2, 1.5]
print("Total: R$", format(quantidade * tabela_precos[codigo - 1], ".2f"))
