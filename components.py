class Components:
    def __init__(self, n):
        self.vanhemmat = list(range(n))
        self.komponentit = n

    # Apufunktio ehtimään parametrina  annetun kaupungin vanhemman
    def find(self, kaupunki):
        if self.vanhemmat[kaupunki] != kaupunki:
            self.vanhemmat[kaupunki] = self.find(self.vanhemmat[kaupunki])
        return self.vanhemmat[kaupunki]

    def add_road(self, kaupunki1, kaupunki2):
        #Yhdistetään kaksi komponenttia päivittämällä niiden juurien vanhemmaksi toisen kaupungin juuri
        juuri1 = self.find(kaupunki1 -1)
        juuri2 = self.find(kaupunki2 -1)

        if juuri1 != juuri2:
            self.vanhemmat[juuri1] = juuri2
            # Vähennetään komponenttien määrää yhdellä kun tie on lisätty kahden kaupungin välille = muodostavat yhdessä yhden komponentin
            self.komponentit -= 1
            
    def count(self):
        return self.komponentit

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count()) # 3
    c.add_road(2, 3)
    print(c.count()) # 3
    c.add_road(4, 5)
    print(c.count()) # 2