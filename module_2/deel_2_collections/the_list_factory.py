def antwoord(a):
    while True:
        getal = input(a)
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal, vul een getal in")

hvllijst = antwoord("hoeveel lijstjes wil je? ")
lengtelijst = antwoord("hoelang moet het lijstje worden? ")

for i in range(1,hvllijst +1):
    print(list(range(i, lengtelijst * i + 1, i )))