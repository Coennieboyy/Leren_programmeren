from fruitmand import fruitmand
from operator import itemgetter

for fruit in sorted(fruitmand, key=itemgetter("weight"), reverse=True):
    print(f"{fruit['name']} : {fruit['weight']/1000}kg")