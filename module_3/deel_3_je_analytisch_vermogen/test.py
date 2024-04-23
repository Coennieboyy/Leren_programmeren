TXT_PIECES = '|'
TXT_SPOONS = 'eetlepel|eetlepels'
TXT_TEASPOONS = 'theelepel|theelepels'
txt = 'kopje|kopjes'




def str_single_plural(amount,  txt: str) -> str:
  split = txt.split(TXT_PIECES, 1)
  if amount >=2:  
    return f"{amount} {split[1]}"
  else:
    return f"{amount} {split[0]}"

print(str_single_plural(2,txt))

