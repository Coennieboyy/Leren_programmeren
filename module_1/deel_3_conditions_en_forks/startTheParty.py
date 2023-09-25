gastheer = input("wie is de gastheer? ")
gasten = int(input("hoeveel gasten zijn er? "))
drank = True
chips = True

if ((gasten >= 4 and gasten <= 20) or gastheer == "coen") and (gastheer == "coen" and drank) or ((gasten >= 4 and gasten <= 20) and drank and chips):
    print('Start the Party')
else:
    print('No Party')