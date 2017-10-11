leeftijd = int(input('geef je leeftijd: '))
paspoort = input('Ben je nederlander? ')
if leeftijd > 17 and paspoort== 'ja':
    print ('gefeliciteerd, je mag stemmen!')
else:
    print('je mag niet stemmen, want je moet nederlander en 18 jaar oud zijn')
