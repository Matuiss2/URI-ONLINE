dias_total = int(input())
anos = dias_total // 365
meses = (dias_total - (365 * anos)) // 30
dias = (dias_total - (365 * anos)) - (30 * meses)
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))
