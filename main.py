import pickle

print("Sveiki atvykę į mini biudžeto programą!\n")

# Bandyti atidaryti esamą failą su duomenimis, jei toks yra
try:
    with open("minibiudzetas.pkl", "rb") as file:
        minibiudzetas = pickle.load(file)
except FileNotFoundError:
    minibiudzetas = []

while True:
    # 1.
    ivestis = input("Įvesti pajamas arba išlaidas (su '-' ženklu), 'tikrinti' peržiūrėjimui arba 'baigti' išėjimui: \n")

    if ivestis.lower() == 'baigti':
        break

    if ivestis.lower() == 'tikrinti':
        # 3.
        print("Įvestos pajamos ir išlaidos:")
        for irasai in minibiudzetas:
            print(irasai)

        # 4.
        balansas = sum(minibiudzetas)
        print(f"Balansas: {balansas}\n")
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
    print(f"Balansas: {balansas}\n")

# 2.
with open("minibiudzetas.pkl", "wb") as file:
    pickle.dump(minibiudzetas, file)

print("Duomenys išsaugoti.")
