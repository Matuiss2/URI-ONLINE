tabela_qntd = {"total": 0}
for i in range(int(input())):
    qntd, tipo = input().split()
    tabela_qntd.setdefault(tipo, 0)
    tabela_qntd[tipo] += int(qntd)
    tabela_qntd["total"] += int(qntd)

coelho, rato, sapo, total = tabela_qntd["C"], tabela_qntd["R"], tabela_qntd["S"], tabela_qntd["total"]
print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\n"
      "Percentual de coelhos: {} %\nPercentual de ratos: {} %\nPercentual de sapos: {} %".format(total, coelho, rato,
       sapo, format(coelho / total * 100, ".2f"), format(rato / total * 100, ".2f"), format(sapo / total * 100, ".2f")))
