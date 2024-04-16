from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input_nr_persons("Ingredienten voor hoeveel personen? ")) # replace this with better input

# ----- CALCULATIONS ----
# calculate factor
if nr_persons != 4:
    calcFactor = nr_persons/4 

# calculate amount_eggs
eggs = round_piece(calcFactor * AMOUNT_EGGS)

# calculate amount_milk
milk = round_quarter(calcFactor * AMOUNT_MILK)

# calculate amount_salt
salt = round_quarter(calcFactor * AMOUNT_SALT)

# calculate amount_pepper
pepper = round_quarter(calcFactor * AMOUNT_PEPPER)

# calculate amount_oil
oil = round_piece(calcFactor * AMOUNT_OIL)

# calculate amount_onions
onions = round_piece(calcFactor * AMOUNT_ONIONS)

# calculate amount_garlics
garlics = round_piece(calcFactor * AMOUNT_GARLICS)

# calculate amount_spinach
spinach = round_piece(calcFactor * AMOUNT_SPINACH)

# calculate amount_paprikas
paprikas = round_piece(calcFactor * AMOUNT_PAPRIKAS)

# calculate amount_cheese
cheese = round_quarter(calcFactor * AMOUNT_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')