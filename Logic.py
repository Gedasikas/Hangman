from Hangman_Images import stages


zodziai = "gedas"
gyvybes = 0
reikiamos_raides = []
buvusios_raides = []
for raide in zodziai:
    reikiamos_raides.append(raide)

while True:
    if gyvybes == 7:
        print(stages[-1])
        print(f"###PRALAIMĖJAI###\nŽodis buvo: {zodziai}")
        break
    else:
        ivesta_raide = input("Įvesk raidę: ").lower()
        if ivesta_raide in reikiamos_raides and ivesta_raide not in buvusios_raides:
            buvusios_raides.append(ivesta_raide)
            print("Teisingai!")
            print(f"Spėtos raidės: {buvusios_raides}")

        elif ivesta_raide not in reikiamos_raides:
            buvusios_raides.append(ivesta_raide)
            gyvybes += 1
            print(f"Neteisingai")
            print(f"Spėtos raidės: {buvusios_raides}")
            print(f"{stages[gyvybes]}")

        elif ivesta_raide in buvusios_raides:
            print("Šitą raidę jau spėjai!")
            print(f"Spėtos raidės: {buvusios_raides}")




