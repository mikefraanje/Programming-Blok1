bestandje = open("/Users/mikefraanje/Desktop/HU/Programming/kaartnummers.txt")

for x in bestandje:
    a,b = x.split(",")
    print(b,'heeft kaartnummer:',a)

print(bestandje.readlines())
