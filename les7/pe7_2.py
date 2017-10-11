# Practice Exercise 7_2 (while-loop)
# Schrijf een nieuw programma waarin de gebruiker een woord moet invoeren. Dit woord moet uit vier
# letters bestaan. Is dat niet zo, dan wordt en foutmelding getoond en moet de gebruiker opnieuw een
# woord invoeren, net zolang totdat er een woord is ingevoerd dat uit vier letters bestaat. Dan eindigt
# het programma. Gebruik in ieder geval een while-loop, gecombineerd met het break-statement!
# Uitvoer:
# Geef een string van vier letters: worst
# worst heeft 5 letters
# Geef een string van vier letters: oliebol
# oliebol heeft 7 letters
# Geef een string van vier letters: drop
# Inlezen van correcte string: drop is geslaagd

def nieuw_programma():
    while True:
        invoer = str(input('Voer een string van 4 karakters in'))
        characters = len(invoer)
        if characters == 4:
            print('Inlezen van correcte string',invoer, 'is geslaagd')
            break
        else:
            print(invoer,'heeft',characters,'letters')

nieuw_programma()
