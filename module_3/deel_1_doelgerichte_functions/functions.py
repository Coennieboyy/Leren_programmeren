def antwoord(a):
    while True:
        vraag = input(a).lower()
        try:
            vraag = int(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul text in")