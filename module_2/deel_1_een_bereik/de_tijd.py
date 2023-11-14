for i in range(1,25):
    if i <= 12:
        print(f"{i}am")
    if i > 12:
        i-=12
        print(f"{i}pm")