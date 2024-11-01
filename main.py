import pickle

# Bandyti atidaryti esamą failą su duomenimis, jei toks yra
try:
    with open("minibiudzetas.pkl", "rb") as file:
        minibiudzetas = pickle.load(file)
except FileNotFoundError:
    minibiudzetas = []

while True:
    # 1.
    ivestis = input("Įveskite pajamas arba išlaidas (su '-' ženklu), 'patikrinti' peržiūrėti arba 'baigti' išėjimui: ")

    if ivestis.lower() == 'baigti':
        break

    if ivestis.lower() == 'patikrinti':
        # 3.
        print("Įvestos pajamos ir išlaidos:")
        for irasai in minibiudzetas:
            print(irasai)

        # 4.
        balansas = sum(minibiudzetas)
        print(f"Balansas: {balansas}")
        continue

    try:
        suma = float(ivestis)
        minibiudzetas.append(suma)
    except ValueError:
        print("Neteisinga įvestis, bandykite dar kartą.")

    # 3.
    print("Įvestos pajamos ir išlaidos:")
    for irasai in minibiudzetas:
        print(irasai)

    # 4.
    balansas = sum(minibiudzetas)
    print(f"Balansas: {balansas}")

# 2.
with open("minibiudzetas.pkl", "wb") as file:
    pickle.dump(minibiudzetas, file)

print("Duomenys išsaugoti.")
