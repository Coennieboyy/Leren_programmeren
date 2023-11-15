dagen = ("maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag")

for i in dagen:
    print(i)
print("hele week\n")

for i in range(7):
    print(dagen[6 - i])
print("hele week andersom\n")

for i in dagen:
    if i in ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]:
        print(i)
print("werkdagen\n")

for i in range(5):
    print(dagen[4 - i])
print("werkdagen andersom\n")

for i in dagen:
    if i in ["zaterdag","zondag"]:
        print(i)
print("weekenddagen\n")

for i in range(2):
    print(dagen[6-i])
print("weekenddagen andersom")
