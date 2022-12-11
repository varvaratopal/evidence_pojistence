from Pojistenec import Pojistenec

class Evidence:
    def __init__(self):
        self.Pojistenec = []
        self.Pojistenec.append(Pojistenec("David", "Capka", 33, 123456789))
        self.Pojistenec.append(Pojistenec("David", "Jancik", 27, 123456788))

    def menu(self):
        print("\nVyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec\n")

        while True:
            try:
                choice = int(input("Zadej výběr:\n"))
            except ValueError:
                print("Nevalidní volba - výběr musí být číslo")
                continue
            else:
                if choice < 1 or choice > 4:
                    print("Nevalidní volba - zadejte číslo z menu")
                    continue
                else:
                    return choice

    def pridatPojistence(self):
        jmeno = input("Zadej jméno pojištěného:\n")
        prijmeni = input("Zadej příjmení pojištěného:\n")
        vek = None
        # Vyžaduje věk dokud uživatel nezadá validní kladné číslo
        while True:
            try:
                vek = int(input("Zadej věk:\n"))
            except ValueError:
                print("Věk musí být kladné číslo")
                continue
            else:
                if vek <= 0:
                    print("Věk musí být kladné číslo")
                    continue
                else:
                    break

        tel_cislo = None
        while True:
            tel_cislo = input("Zadej telefonní číslo:\n")
            # Telefonní číslo musí být 9 znaků dlouhé číslo
            if tel_cislo.isnumeric() and len(tel_cislo) == 9:
                break
            else:
                print("Neplatné telefonní číslo")
                continue
        self.Pojistenec.append(Pojistenec(jmeno, prijmeni, vek, tel_cislo))
        print("Nový pojištěnec přidán.")
        input("Pokračujte libovolnou klávesou...\n")

    def vypsat(self):
        for Pojistence in self.Pojistenec:
            print(Pojistence)
        input("Pokračujte libovolnou klávesou...\n")

    def vyhledat(self):
        vyhledani = input("Zadejte jméno pojisteného:\n")
        vyhledani = input("Zadej příjmení:\n")
        for Pojistence in self.Pojistenec:
            if Pojistence.jmeno == vyhledani or Pojistence.prijmeni == vyhledani:
                print(Pojistence)
        input("Pokračujte libovolnou klávesou...\n")
