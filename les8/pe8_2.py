import random

worp = 0

def monopolyworp():

    global worp
    for x in range(2):
        dobbelsteen1 = random.randint(1,6)
        dobbelsteen2 = random.randint(1,6)
        worp +=1
    print(dobbelsteen1,'+',dobbelsteen2,'=',dobbelsteen1 + dobbelsteen2)
    if dobbelsteen1 == dobbelsteen2:
        print(dobbelsteen1,'+',dobbelsteen2,'=',dobbelsteen1 + dobbelsteen2)
        monopolyworp()
        if worp == 4:
            print('Ga direct naar de gevangenis')

monopolyworp()

