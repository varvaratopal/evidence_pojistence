class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return "{jmeno}\t{prijmeni}\t{vek}\t{tel_cislo}".format(jmeno=self.jmeno, prijmeni=self.prijmeni, vek=self.vek, tel_cislo=self.tel_cislo)
