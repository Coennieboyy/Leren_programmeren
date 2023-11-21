dagen = ("maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag")

for i in dagen:
    print(i)
print("hele week\n")

for i in range(6,-1,-1):
    print(dagen[i])
print("hele week andersom\n")

for i in range(0,4):
        print(dagen[i])
print("werkdagen\n")

for i in range(5,7):
    print(dagen[i])
print("werkdagen andersom\n")

for i in dagen:
    if i in ["zaterdag","zondag"]:
        print(i)
print("weekenddagen\n")

for i in range(6,4,-1):
    print(dagen[i])
print("weekenddagen andersom")
