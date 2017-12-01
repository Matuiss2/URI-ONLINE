value = eval(input())

cem = cinquenta = vinte = dez = cinco = dois = um = 0
cincents = vintecincents = dezcents = cincocents = cents = 0

value = float("%.2f" % value)
if int(value / 100) >= 1:
    cem = int(value / 100)
    value -= cem * 100

value = float("%.2f" % value)
if int(value / 50) >= 1:
    cinquenta = int(value / 50)
    value -= cinquenta * 50

value = float("%.2f" % value)
if int(value / 20) >= 1:
    vinte = int(value / 20.00)
    value -= vinte * 20

value = float("%.2f" % value)
if int(value/10) >= 1:
    dez = int(value / 10)
    value -= dez * 10.00

value = float("%.2f" % value)
if int(value/5) >= 1:
    cinco = int(value / 5)
    value -= cinco * 5

value = float("%.2f" % value)
if int(value/2) >= 1:
    dois = int(value / 2)
    value -= dois * 2

value = float("%.2f" % value)
if int(value / 1) >= 1:
    um = int(value / 1)
    value -= um * 1

value = float("%.2f" % value)
if int(value / 0.50) >= 1:
    cincents = int(value/0.50)
    value -= cincents*0.50

value = float("%.2f" % value)
if int(value / 0.25) >= 1:
    vintecincents = int(value / 0.25)
    value -= vintecincents * 0.25

value = float("%.2f" % value)
if int(value / 0.10) >= 1:
    dezcents = int(value / 0.10)
    value -= dezcents * 0.10

value = float("%.2f" % value)
if int(value / 0.05) >= 1:
    cincocents = int(value / 0.05)
    value -= cincocents * 0.05

value = float("%.2f" % value)
if int(value / 0.01) >= 0.998:
    cents = int(value / 0.01)
    value -= cents * 0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % um)
print("%d moeda(s) de R$ 0.50" % cincents)
print("%d moeda(s) de R$ 0.25" % vintecincents)
print("%d moeda(s) de R$ 0.10" % dezcents)
print("%d moeda(s) de R$ 0.05" % cincocents)
print("%d moeda(s) de R$ 0.01" % cents)
