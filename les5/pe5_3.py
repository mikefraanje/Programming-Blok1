bestandje = open("/Users/mikefraanje/Desktop/HU/Programming/kaartnummers.txt")

regels = 0
hoogste = 0
regelnummer = 0

for x in bestandje:
    regels += 1

    a,b = x.split(",")
    if int(a) > hoogste:
        hoogste = int(a)
        regelnummer = regels

print('Deze file telt', regels, 'regels','\n','Het grootste kaarnummer is:', 'en dat staat op regel',regelnummer)
