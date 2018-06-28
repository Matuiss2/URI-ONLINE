tabela_combustivel, comando = {"1": 0, "2": 0, "3": 0}, 0
while comando != "4":
    comando = input()
    if comando in tabela_combustivel.keys():
        tabela_combustivel[comando] += 1
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(tabela_combustivel["1"], tabela_combustivel["2"],
                                                                    tabela_combustivel["3"]))
