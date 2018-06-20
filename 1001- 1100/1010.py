cod_peca1, qntd_peca1, valor_peca1 = input().split()
cod_peca2, qntd_peca2, valor_peca2 = input().split()
print("VALOR A PAGAR: R$", format((int(qntd_peca1) * float(valor_peca1)) + (int(qntd_peca2) * float(valor_peca2)), ".2f"))
