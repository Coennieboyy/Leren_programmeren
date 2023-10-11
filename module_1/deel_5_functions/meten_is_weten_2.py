def getal(nr1, nr2):

    if nr1 > nr2:
      return print(f"Maximum: {nr1} en minimum: {nr2}")
    elif nr1 < nr2:
      return print(f"Maximum: {nr2} en minimum: {nr1}")
    else:
       return print("Beide getallen zijn even groot")



nr1 = int(input("vul een geheel getal in. "))
nr2 = int(input("vul nog een geheel getal in. "))

getal(nr1,nr2)