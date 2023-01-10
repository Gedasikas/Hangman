from Hangman_Images import stages
import re, random
class Spejamas_zodis:
    def __init__(self, zodis):
        self.zodis = zodis
        self.reikiamos_raides = self.sugen_reik_raid()
        self.buvusios_raides = []
        self.ieskomas = self.bruksniuotas()

    def sugen_reik_raid(self):
        l = []
        for raide in self.zodis:
            l.append(raide)
        return l

    def bruksniuotas(self):
        tuscias = ""
        for raid in self.zodis:
            tuscias += "_"
        return tuscias

    def nezinomos_raid(self, spejimas):
        list_size = len(self.reikiamos_raides)
        l = []
        for itr in range(list_size):
            if zodis.reikiamos_raides[itr] == spejimas:
                l.append(itr)
        for i in l:
            self.ieskomas = self.ieskomas[:i] + spejimas + self.ieskomas[i + 1:]
        return self.ieskomas
# -----------------
with open("Zodziai.txt", "r", encoding="UTF-8") as failas:
    tekstas = failas.read()
formatas = re.compile("\w{4,}")
zodziai = formatas.findall(tekstas)
ieskomas_zodis = (random.choice(zodziai)).lower()
# ----------------
zodis = Spejamas_zodis(ieskomas_zodis)
gyvybes = 0
print(f"Žodis: {zodis.ieskomas}")
# ------------------
while True:
    if gyvybes == 7:
        print(stages[-1])
        print(f"###PRALAIMĖJAI###\nŽodis buvo: {zodis.zodis}")
        break
    elif zodis.ieskomas == zodis.zodis:
        print(f"LAIMĖJAI!!!\nŽodis buvo: {zodis.zodis}")
        break
    else:
        userput = input("Spėti raidę: q\nSpėti žodį: w\nTavo Įvedimas:")
        print()
    match userput:
        case "q":
            while True:
                ivesta_raide = input("Įvesk raidę: ").lower()
                print()
                if ivesta_raide in zodis.reikiamos_raides and ivesta_raide not in zodis.buvusios_raides:
                    print("Teisingai!")
                    zodis.buvusios_raides.append(ivesta_raide)
                    print(f"Žodis: {zodis.nezinomos_raid(ivesta_raide)}")
                    print(f"Spėtos raidės: {zodis.buvusios_raides}")
                    print()
                    break
                elif ivesta_raide not in zodis.reikiamos_raides:
                    gyvybes += 1
                    print(f"Neteisingai")
                    print(f"{stages[gyvybes]}")
                    print(f"Žodis: {zodis.nezinomos_raid(ivesta_raide)}")
                    zodis.buvusios_raides.append(ivesta_raide)
                    print(f"Spėtos raidės: {zodis.buvusios_raides}")
                    print()
                    break
                elif ivesta_raide in zodis.buvusios_raides:
                    print("Šitą raidę jau spėjai, rinkis kitą!")
                    print(f"Žodis: {zodis.nezinomos_raid(ivesta_raide)}")
                    print(f"Spėtos raidės: {zodis.buvusios_raides}")
                    print()
                    break
        case "w":
            irasytas = input("Tavo spėjamas žodis: ").lower()
            print()
            if irasytas == zodis.zodis:
                print(f"TEISINGAI!\nŽodis buvo: {zodis.zodis}")
                break
            else:
                print(stages[-1])
                print(f"###PRALAIMĖJAI###\nŽodis buvo: {zodis.zodis}")
                break
