# Schrijf een nieuw programma waarin een list met minimaal 10 strings wordt ingelezen. Het programma
# plaatst alle vier-letter strings uit de ingelezen list in een nieuwe list en drukt deze af. Inlezen van een
# lijst kan met eval(input("Geef lijst met minimaal 10 strings: ")).

lijst = ["boter", "kaas", "bier", "pizza",
"thee", "drop", "koek", "cola", "boterham", "wijn"]

nieuwe_lijst=[]

for x in lijst:
    characters = len(x)
    if characters == 4:
        nieuwe_lijst.append(x)

print(nieuwe_lijst)
