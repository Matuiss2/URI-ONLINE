j = 7
for i in range(1, 10, 2):
    for k in range(3):
        print("I=" + str(i), "J=" + str(j))  # Converti para str para grudar com o +
        j -= 1
    j += 5
