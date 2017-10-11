invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

nieuwe_lijst=invoer.split('-')
nieuwe_lijst.sort()

print("Gesorteerde lijst:",nieuwe_lijst)
print("Grootste getal:",max(nieuwe_lijst),"en Kleinste getal:",min(nieuwe_lijst))
aantal_getallen = len(nieuwe_lijst)

hele_nieuwelijst = []

for x in nieuwe_lijst:
    hele_nieuwelijst.append(int(x))

som = sum(hele_nieuwelijst)
print("Aantal getallen",aantal_getallen,"en Som van de getallen",som)
gemiddelde=som/aantal_getallen
print("Gemiddelde:",gemiddelde)
