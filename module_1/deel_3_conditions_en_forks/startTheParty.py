gastheer = input("wie is de gastheer? ").lower()
gasten = int(input("hoeveel gasten zijn er? "))
drank = True
chips = True

if (((gasten >= 4 and gasten <= 20) or gastheer) and (gastheer and drank) or ((gasten >= 4 and gasten <= 20) and drank and chips)) and gastheer != "bouman":
    print('Start the Party')
else:
    print('No Party')