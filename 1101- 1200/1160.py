for i in range(int(input())):
    anos = 0
    populacao1, populacao2, crescimento1, crescimento2 = map(float, input().split())
    while populacao2 >= populacao1:
        if anos > 99:
            print("Mais de 1 seculo.")
            break
        populacao1 += int(populacao1 * crescimento1 / 100)
        populacao2 += int(populacao2 * crescimento2 / 100)
        anos += 1
    else:
        print(anos, "anos.")
