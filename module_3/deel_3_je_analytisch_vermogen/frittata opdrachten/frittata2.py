from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input_nr_persons("Ingredienten voor hoeveel personen? ")) # replace this with better input

# ----- CALCULATIONS ----
# calculate factor
if nr_persons != RECIPE_PERSONS:
    calcFactor = nr_persons/RECIPE_PERSONS 
else:
    calcFactor = 1

# calculate amount_eggs
eggs = round_piece(calcFactor * AMOUNT_EGGS)

# calculate amount_milk
milk = round_quarter(calcFactor * AMOUNT_MILK)

# calculate amount_salt
salt = round_quarter(calcFactor * AMOUNT_SALT)

# calculate amount_pepper
pepper = round_quarter(calcFactor * AMOUNT_PEPPER)

# calculate amount_oil
oil = round_quarter(calcFactor * AMOUNT_OIL)

# calculate amount_onions
onions = round_piece(calcFactor * AMOUNT_ONIONS)

# calculate amount_garlics
garlics = round_piece(calcFactor * AMOUNT_GARLICS)

# calculate amount_spinach
spinach = round_quarter(calcFactor * AMOUNT_SPINACH)

# calculate amount_paprikas
paprikas = round_piece(calcFactor * AMOUNT_PAPRIKAS)

# calculate amount_cheese
cheese = round_quarter(calcFactor * AMOUNT_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print(f"{str_amount_fraction(eggs)}{str_units(eggs, UNIT_EGGS)} {str_single_plural(eggs,TXT_EGGS)}")
print(f"{str_amount_fraction(milk)} {str_units(milk, UNIT_MILK)} {str_single_plural(milk, TXT_MILK)}")
print(f"{str_amount_fraction(salt)} {str_units(salt, UNIT_SALT)} {str_single_plural(salt, TXT_SALT)}")
print(f"{str_amount_fraction(pepper)} {str_units(pepper, UNIT_PEPPER)} {str_single_plural(pepper, TXT_PEPPER)}")
print(f"{str_amount_fraction(oil)} {str_units(oil, UNIT_OIL)} {str_single_plural(oil, TXT_OIL)}")
print(f"{str_amount_fraction(onions)}{str_units(onions, UNIT_ONIONS)} {str_single_plural(onions, TXT_ONIONS)}")
print(f"{str_amount_fraction(garlics)}{str_units(garlics, UNIT_GARLICS)} {str_single_plural(garlics, TXT_GARLICS)}")
print(f"{str_amount_fraction(paprikas)}{str_units(paprikas, UNIT_PAPRIKAS)} {str_single_plural(paprikas, TXT_PAPRIKAS)}")
print(f"{str_amount_fraction(spinach)} {str_units(spinach, UNIT_SPINACH)} {str_single_plural(spinach, TXT_SPINACH)}")
print(f"{str_amount_fraction(cheese)} {str_units(cheese, UNIT_CHEESE)} {str_single_plural(cheese, TXT_CHEESE)}")
print('-----------------------------------------------')