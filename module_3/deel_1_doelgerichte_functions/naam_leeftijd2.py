from functions import Persoonlijke_gegevens

persoon = Persoonlijke_gegevens()
for personen in persoon:
    print(f" in {personen['woonplaats']} woont, de {personen['leeftijd']} jarige {personen['naam']}.")

print(persoon) 