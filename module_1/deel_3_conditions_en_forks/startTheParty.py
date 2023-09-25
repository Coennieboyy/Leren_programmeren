gastheer = True
gasten = True
drank = True
chips = True

if (gasten or gastheer) and (gastheer and drank) or (gasten and drank and chips):
    print('Start the Party')
else:
    print('No Party')
