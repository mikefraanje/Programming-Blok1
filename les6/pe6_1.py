def seizoen(maandnummer):
    maandnummer = int(input("Wat is het maandnummer"))

    if maandnummer >= 3 and maandnummer <6:
        print('het is lente')
    elif maandnummer >=6 and maandnummer < 9:
        print('het is zomer')
    elif maandnummer >=9 and maandnummer < 12:
        print('het is herfst')
    else:
        print('het is winter')
        
seizoen(1)
