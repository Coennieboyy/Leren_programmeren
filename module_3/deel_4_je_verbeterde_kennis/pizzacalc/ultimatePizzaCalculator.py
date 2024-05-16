from Functions import *

total = 0
sizes = {
    "small" : {"amount":0, "price":8.99},
    "medium": {"amount":0, "price":18.00},
    "large" : {"amount":0, "price":23.80}
}

for size in sizes:
    vraag = antwoordfloat(f"hoeveel {size} wil je? ")
    sizes[size]["amount"] += vraag

print("------------------------------------------")
for size in sizes:
    calculations = sizes[size]["amount"] * sizes[size]["price"]
    print(f"{sizes[size]['amount']} x {size} pizza's: {calculations}")
    total = total + calculations
print()     
print(f"totaal: {round(total,2)}")
print("------------------------------------------")