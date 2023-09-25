a = int(input("vul een geheel getal in. "))
b = int(input("vul nog een geheel getal in. "))

if a > b:
    max = a
    min = b
    print(f"a is het grootste getal: ' gevolgd door de waarde van {max}")
elif a < b:
    max = b
    min = a
    print(f"a is het kleinste getal:  gevolgd door de waarde van {min}")
else:
    print("a en b zijn even groot")

print(f"Het minimum is:  gevolgd door de waarde van {min}")
print(f"Het maximum is:  gevolgd door de waarde van {max}")