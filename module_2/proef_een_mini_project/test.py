import random


lijst = ["ballen", "coen"]
lijst2 = lijst.copy()
dic = {}
input = input("")
for i in range(len(lijst)):
    if lijst[i] != lijst2[i]:
        dic.update({lijst[i]: lijst2[i]})
    else:
        random.shuffle(lijst2)

print(dic)
