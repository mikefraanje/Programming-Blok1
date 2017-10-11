# Practice Exercise 7_3 (dict)
# Maak een dictionary aan met cijfers voor een cursus. De studentnamen zijn de sleutels en de cijfers
# zijn de waarden in de dictionary. Zorg dat er minimaal 8 cijfers in de dictionary staan. Schrijf vervolgens
# code om op basis van die dictionary alle cijfers (met naam) boven een 9,0 te printen.

cijfers = {
    'piet': 8.6,
    'peter': 9.9,
    'jan': 6.6,
    'henk': 7.0,
    'willem': 9.5,
    'jantje': 8.4,
    'klaas': 2.9,
    'tim': 9.2,
    'ties': 5.5,
    }

for key, value in cijfers.items():
    if value > float(9.0):
        print(key,value)
