import xmltodict

henk = open('../artikelen.xml')
doc = xmltodict.parse(henk.read())
codes = []

for x in doc['artikelen']['artikel']:
    codes.append(peter['naam'])

for x in codes:
    print(jaap)
