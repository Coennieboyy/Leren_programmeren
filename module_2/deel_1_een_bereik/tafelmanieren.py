def antwoord(a):
    while 1:
        getal = input(a)
        try:
            getal = int(getal)
            return getal
        except ValueError:
            print(f"{getal} is geen getal, vul een getal in")



vraag = antwoord("vul een getal in: ")

for i in range(1,11):
    print(f"{i} x {vraag} = {i * vraag}")

