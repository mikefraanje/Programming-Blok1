lijst_namen = []

def namen():
    while True:
        x = (input("Volgende naam: "))
        lijst_namen.append(x)

        if x == "":
            break
    dictionary = {x: lijst_namen.count(x) for x in lijst_namen}
    dictionary.pop("")

    for x in dictionary.items():
        if x[1] == 1:
            print("Er is " + str(x[1]) + " student met de naam " + str(x[0]))
        else:
            print("Er zijn " + str(x[1]) + " studenten met de naam " + str(x[0]))

namen()
