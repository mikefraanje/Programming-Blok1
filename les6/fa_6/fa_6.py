# kluizen = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']

bestand = open("/Users/mikefraanje/PycharmProjects/untitled1/fa_6/kluizen.txt")

# def kluis_openen():

# def kluis_teruggeven():

def toon_aantal_kluizen_vrij():
    aantal = len(bestand.readlines())
    print("Er zijn nog", aantal, "kluizen vrij")

toon_aantal_kluizen_vrij()

def nieuwe_kluis():
    kluizen_lijst = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    print(bestand.readlines())
    for x in bestand:
        print('piep')



nieuwe_kluis()
# def keuze_menu(menukeuze):
#     optie=int(input('maak een keuze uit het menu'))
#     if optie == 1:
#         toon_aantal_kluizen_vrij()
#     elif optie == 2:
#         nieuwe_kluis()
#     elif optie == 3:
#         kluis_openen()
#     else:
#         kluis_teruggeven()
#
#
# keuze_menu(1)
