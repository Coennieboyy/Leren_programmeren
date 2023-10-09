def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount1 = float(input(f'Hoeveel ijsjes van {convertToEuroText(SMALL_PRICE)} wil je bestellen? '))
amount2 = float(input(f'fEn hoeveel ijsjes van {convertToEuroText(MEDIUM_PRICE)} wil je bestellen? '))
totalPrice = (amount1 * SMALL_PRICE) + (amount2 * MEDIUM_PRICE)

print(f'Dat is dan {(convertToEuroText(totalPrice))} totaal')