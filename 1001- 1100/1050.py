ddd = int(input())
tabela = {61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro",
          32: "Juiz de Fora", 19: "Campinas", 27: "Vitoria", 33: "Belo Horizonte"}
if ddd in tabela.keys():
    print(tabela[ddd])
else:
    print("DDD nao cadastrado")
