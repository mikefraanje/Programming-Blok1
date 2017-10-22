def test(bestandnaam):
    with open(bestandnaam) as f:
        mylist = f.read().splitlines()
    return mylist

score = test('gamers.csv')

hoogstescore = 0

for huidigeregel in score:
    woorden = huidigeregel.split(';')
    for x in woorden:
        if int(woorden[2]) > hoogstescore:
            hoogstescore = int(woorden[2])
            print(hoogstescore)

print('De hoogste score is: ' + str(hoogstescore) + ' op ' + datum + ' behaald door ' + naam)
