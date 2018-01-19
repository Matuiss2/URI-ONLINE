inutil = input()
data = list(map(int, input().split()))
print(data.index(min(data)) + 1)  # +1 pois index() conta a posição a partir do 0