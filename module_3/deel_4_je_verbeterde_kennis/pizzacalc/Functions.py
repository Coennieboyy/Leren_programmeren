def antwoordfloat(a)-> float:
    while True:
        vraag = input(a)
        try:
            vraag = float(vraag)
            return vraag
        except ValueError:
            print(f"{vraag} is geen geldig antwoord, vul cijfer in")

def antwoord(a:str)-> str:
    while True:
        string = input(a).lower()
        if str.isalpha(string) == True:
            return string
        else:
            print(f"{string} is geen geldig antwoord, vul tekst in")