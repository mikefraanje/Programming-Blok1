cijferICOR = float(input('Wat is je cijfer voor ICOR?: '))
x = 30
beloningICOR =  cijferICOR * x
beloning = 'beloning €'
print(beloning, beloningICOR)

cijferPROG = float(input('Wat is je cijfer voor PROG: '))
beloningPROG  = cijferPROG * x
print(beloning, beloningPROG)

cijferCSN = float(input('Wat is je cijfer voor CSN?: '))
beloningCSN = cijferCSN * x
print(beloning, beloningCSN)

gemiddelde = beloningICOR + beloningPROG + beloningCSN
print('de gemiddelde beloning is:€ ', gemiddelde / 3)

totalevergoeding = beloningICOR + beloningPROG + beloningCSN
print('uw totale vergoeding is:€ ', totalevergoeding)

gemiddeld_cijfer = (cijferICOR + cijferPROG + cijferCSN) / 3
print('mijn cijfers gemiddeld is een', gemiddeld_cijfer, 'en dat levert een beloning op van: €', totalevergoeding)
