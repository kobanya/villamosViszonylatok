import magyar

varosok = {} # városok szótár létrehozása
for vonal in magyar.villamos.values():
    varos = vonal["varos"]
    if varos not in varosok:
        varosok[varos] = []
    varosok[varos].append(str(vonal["viszonylat"]))

for varos, vonalszamok in varosok.items():
    print(varos + ", " + ", ".join(vonalszamok))

print("-------------------------------------------------------------------------------------")

# Bekérjük a felhasználó által kiválasztott várost és vonalszámot az input függvénnyel, és az elválasztó karakterrel elválasztva, nagy betűsítve
varos_vonalszam = input("Kérlek add meg a várost és vonalszámot, szóközzel vagy vesszővel elválasztva: ").capitalize().strip()

if "," in varos_vonalszam:
    varos, vonalszam = varos_vonalszam.split(",")
elif " " in varos_vonalszam:
    varos, vonalszam = varos_vonalszam.split()
else:
    print("Hibás formátum! Használj vesszőt vagy szóközt a két érték elválasztásához!")

# Ellenőrizzük, hogy a megadott vonalszám a helyes formátumban van-e
try:
    vonalszam = int(vonalszam)
except ValueError:
    print("A vonalszám csak szám lehet!")
    exit()
# Ellenőrizzük, hogy a megadott város és vonalszám létezik-e a szótárban
if varos in varosok and str(vonalszam) in varosok[varos]:
    print(f'{varos} { vonalszam } adatai: \n')
else:
    print("A megadott vonalszám nem található a(z) " + varos + " városban.")

# Keresd meg a megfelelő vonalat a villamos szótárban a megadott városnév és vonalszám alapján
vonal = None
for vonal_neve, vonal_adatok in magyar.villamos.items():
    if vonal_adatok["varos"] == varos and vonal_adatok["viszonylat"] == vonalszam:
        vonal = vonal_adatok
        break

# Ellenőrizd, hogy talált-e a keresés során vonalat a megadott városnévvel és vonalszámmal
if vonal is None:
    print("Nem található vonal a(z) " + varos + " városban a(z) " + str(vonalszam) + " számú viszonylattal.")
else:
    # Kiírjuk a kiválasztott vonal adatait
    print("Indulás: " + vonal["indulas"])
    print("Érkezés: " + vonal["erkezes"])
    print("Menetidő: " + str(vonal["menetido"]) + " perc.\n")
