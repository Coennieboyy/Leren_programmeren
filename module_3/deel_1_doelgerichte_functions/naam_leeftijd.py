from functions import Persoonlijke_gegevens

persoon = Persoonlijke_gegevens()
for personen in persoon:
    print(f"{personen['naam']}, die in {personen['woonplaats']} woont,  is {personen['leeftijd']} jaar.")

print(persoon) 