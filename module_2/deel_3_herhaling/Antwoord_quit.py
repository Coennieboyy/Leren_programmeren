hvlvragen = 0

while True:
    vraag = input("? ").lower()
    hvlvragen +=1
    if vraag == "quit":
        print(f"je hebt {hvlvragen} keer deze vraag beantwoordt")
        break
    
