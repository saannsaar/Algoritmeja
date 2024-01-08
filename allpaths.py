class AllPaths:
    def __init__(self, n):
        self.solmut = n
        self.verkko = {i: [] for i in range(1, n + 1)}

    def add_edge(self, a, b):
        self.verkko[a].append(b)

    def count(self):
        # Alustetaan vastaus objektina missä avaimena on solmu ja avaimen arvona on alustava polkujen määrä
        self.vastaus = {i: -1 for i in range(1, self.solmut + 1)}
        lopullinenVastaus = 0

        #Luupataan kaikki solmut ja lasketaan polut 
        for solmu in range(1, self.solmut + 1):
            lopullinenVastaus += self.count_from(solmu)

        return lopullinenVastaus

    def count_from(self, solmu):
        #Jos polut solmusta on jo laskettu palautetaan 
        if self.vastaus[solmu] != -1:
            return self.vastaus[solmu]

        polkujenMaara = 1  # Yksittäinen solmu lasketaan poluksi, siksi alustetaan ykköseksi
        for viereinen in self.verkko[solmu]:
            polkujenMaara += self.count_from(viereinen)
        self.vastaus[solmu] = polkujenMaara
        return polkujenMaara


if __name__ == "__main__":
    a = AllPaths(4)
    a.add_edge(1, 2)
    a.add_edge(1, 3)
    a.add_edge(2, 4)
    a.add_edge(3, 4)
    print(a.count())  # Output: 10
    a.add_edge(2, 3)
    print(a.count())  # Output: 14
