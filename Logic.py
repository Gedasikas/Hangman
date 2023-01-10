from Hangman_Images import stages


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


zodis = Spejamas_zodis("gedas")
gyvybes = 0

# while True:
#     userput = input("Spėti raidę: 1\nSpėti žodį: 2\nTavo Įvedimas:")
#     match userput:
#         case "1":
while True:
    if gyvybes == 7:
        print(stages[-1])
        print(f"###PRALAIMĖJAI###\nŽodis buvo: {zodis.zodis}")
        break
    elif zodis.ieskomas == zodis.zodis:
        print(f"LAIMĖJAI!!!\nŽodis buvo: {zodis.zodis}")
        break
    else:
        ivesta_raide = input("Įvesk raidę: ").lower()
        print()
        if ivesta_raide in zodis.reikiamos_raides and ivesta_raide not in zodis.buvusios_raides:
            print("Teisingai!")
            zodis.buvusios_raides.append(ivesta_raide)
            print(f"Žodis: {zodis.nezinomos_raid(ivesta_raide)}")
            print(f"Spėtos raidės: {zodis.buvusios_raides}")
            print()
        elif ivesta_raide not in zodis.reikiamos_raides:
            gyvybes += 1
            print(f"Neteisingai")
            print(f"{stages[gyvybes]}")
            print(f"Žodis: {zodis.nezinomos_raid(ivesta_raide)}")
            zodis.buvusios_raides.append(ivesta_raide)
            print(f"Spėtos raidės: {zodis.buvusios_raides}")
            print()
        elif ivesta_raide in zodis.buvusios_raides:
            print("Šitą raidę jau spėjai, rinkis kitą!")
            print(f"Žodis: {zodis.nezinomos_raid(ivesta_raide)}")
            print(f"Spėtos raidės: {zodis.buvusios_raides}")
            print()
# case "2":
#     pass
# case "3":
#     break
