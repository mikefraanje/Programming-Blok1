# def kwadraten_som(grondgetallen):
#     print(sum(getal*2 for getal in grondgetallen if getal > 0))
#
# kwadraten_som([34,-44,22,11])


def kwadraten_som(lijst):
    totaal=0
    for getal in lijst:
        if getal > 0:
            totaal+=(getal**2)
    return totaal

print(kwadraten_som([5, 3, 2, -10]))
