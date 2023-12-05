#i = 1
#while i < 13:
#    print(f"{i}am")
#    i += 1

#t = 1
#while t < 13:
#    print(f"{t}pm")
#    t += 1


i = 1
while i <= 24:
    if i <= 12:
        print(f"{i}am")
        i += 1
    elif i > 12:
        print(f"{i - 12}pm")
        i += 1
        