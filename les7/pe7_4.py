# Practice Exercise 7_4 (file & dict)
# Een ‘ticker symbol’ is een unieke afkorting om aandelen van een bepaald bedrijf aan de beurs te
# identificeren. YHOO is bijvoorbeeld het ticker symbol van Yahoo, terwijl GOOG dat is voor Google.
# Gegeven is het onderstaande bestaand met ticker symbols:
# YAHOO:YHOO
# GOOGLE INC:GOOG
# Harley-Davidson:HOG
# Yamana Gold:AUY
# Sotheby's:BID
# inBev:BUD
# Schrijf een functie ticker(filename). De functie leest uit de file zowel de bedrijfsnaam als het
# bijbehorende ticker-symbool en slaat die op in een dictionary. Dit is de return-waarde van de functie.
# Schrijf nu ook een programma die deze functie gebruikt om als iemand een ticker-symbool ingeeft de
# bedrijfsnaam te printen, en andersom. Het programma stopt hierna:
# Uitvoer:
# Enter Company name: YAHOO
# Ticker symbol: YHOO
# Enter Ticker symbol: BUD
# Company name: inBev


# company_list = {
#     'YAHOO': 'YHOO',
#     'GOOGLE INC': 'GOOG',
#     'Harley-Davidson' :'HOG',
#     'Yamana Gold': 'AUY',
#     "Sotheby's": 'BID',
#     'inBev': 'BUD',
#     }

# bedrijfsnaam = input('Voer hier een bedrijfsnaam in').upper()

def ticker(filename):
    with open('ticker.txt','r') as file:
        ticker = {}
        file = file.readlines()
        for line in file:
            line = line.split(':')

        print(line)


ticker(1)
