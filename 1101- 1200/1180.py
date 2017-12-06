# Esse val deve ser para facilitar p qm vai fazer o ex pelo método de iteração, mas no meu método esse valor é inutil
inutil = int(input())
data = input().split()  # Separa os valores e tranformam em itens de uma lista(serão valores str)
menor = min(map(int, data))  # Usa o map para converter os itens para int o usa o min para pegar o menor
print("Menor valor:", menor)
print("Posicao:", data.index(str(menor)))
# O método index pega a posição do item str dentro dos (), só é possível pois os valores são todos distintos
