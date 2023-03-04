# Ratkaisu
# Tätä sivustolla en saanut toimimaan...

# Vastaus ehkä on: heisanyt123voihyvin
# Lukuna: 733742598348518068380937903490247877054607178996642679707678827022708178001310216935252214348434279832741522437036812568193956002869955826358882233317236785293611860144726281220

# Muuntotaulukko
muuntotaulukko = {
    32: " ", 97: "a", 98: "b", 99: "c", 100: "d",
    101: "e", 102: "f", 103: "g", 104: "h", 105: "i",
    106: "j", 107: "k", 108: "l", 109: "m", 110: "n",
    111: "o", 112: "p", 113: "q", 114: "r", 115: "s",
    116: "t", 117: "u", 118: "v", 119: "w", 120: "x",
    121: "y", 122: "z"
}

# Salainen viesti
s = 85428277862587239591968124579786099007709414278223047737899318765259424056436086074826093092150818499345040297473507839007632632095558200735189531211857679546669771791600041613523605832579335482328444517404371063136115723068982913626804303813782231498500488302844347689387955529396562717610808940562862565420

# Muunnetaan salainen viesti lukujen listaksi
viesti = list(str(s))

# Puretaan viesti takaisin merkkijonoksi
purettu_viesti = ""
for i in range(0, len(viesti), 2):
    merkki = muuntotaulukko[int(viesti[i] + viesti[i+1])]
    purettu_viesti += merkki

# Tulostetaan purettu viesti
print("Purettu viesti (lukuna):", int(purettu_viesti))

# Muutetaan viesti takaisin merkkijonoksi
teksti_viesti = ""
for i in range(0, len(viesti), 2):
    merkki = muuntotaulukko[int(viesti[i] + viesti[i+1])]
    teksti_viesti += merkki

# Tulostetaan viesti tekstinä
print("Purettu viesti (tekstinä):", teksti_viesti)

