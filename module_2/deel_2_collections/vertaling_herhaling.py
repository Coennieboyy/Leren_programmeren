#auto's rijden op hoge snelheid

veranderwoorden={
    "auto's": "vliegtuigen",
    "rijden": "vliegen",
    "hoge": "extreme",
    "snelheid": "snelheden"
}

zin = input("geef een zin op? ").split(' ')
nieuwezin = ""
for woord in zin:
    if woord in veranderwoorden:
        woord = veranderwoorden[woord]
    nieuwezin = nieuwezin + woord + " "
print(nieuwezin)