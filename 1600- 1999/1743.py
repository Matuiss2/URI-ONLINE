plug1 = input().split()
plug2 = input().split()
conta = 0
for i in range(5):
    if plug1[i] != plug2[i]:  # Se os plugs da mesma posição forem diferentes eles se conectam
        conta += 1  # Conta todos os que se conectam
if conta == 5:  # Se 5 se conectarem as 2 tomadas são compatíveis
    print("Y")
else:
    print("N")
