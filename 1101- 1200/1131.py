qntd, inter, gremio, empates, encerramento = 0, 0, 0, 0, 0
while encerramento != 2:
    gols_inter, gols_gremio = map(int, input().split())
    qntd += 1
    if gols_inter == gols_gremio:
        empates += 1
    elif gols_inter > gols_gremio:
        inter += 1
    else:
        gremio += 1
    encerramento = int(input("Novo grenal (1-sim 2-nao)\n"))

print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(qntd, inter, gremio, empates))
if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")