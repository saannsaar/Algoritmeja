import heapq
from collections import defaultdict

class TrainPrices:
    def __init__(self):
        self.kaupungit = []
        self.junaYhteydet = {}

    def add_city(self, kaupunki):
        if kaupunki not in self.kaupungit:
            self.kaupungit.append(kaupunki)
            self.junaYhteydet[kaupunki] = {}

    def add_train(self, city1, city2, hinta):
        if city2 not in self.junaYhteydet[city1] or hinta < self.junaYhteydet[city1][city2]:
            self.junaYhteydet[city1][city2] = hinta
            self.junaYhteydet[city2][city1] = hinta

    def find_prices(self):
        # Järjestetään kaupunkien nimet aakkosjärkkään
        jarjKaupungit = sorted(self.kaupungit)
        halvimmatReitit = [[None] + jarjKaupungit]
        for lahtoKaupunki in jarjKaupungit:
            matka = {kaupunki: float('inf') for kaupunki in jarjKaupungit}
            edellinen = {kaupunki: None for kaupunki in jarjKaupungit}
            matka[lahtoKaupunki] = 0
            prJono = [(0, lahtoKaupunki)]

            while prJono:
                matkaLahtopisteestaNyt, lahtoPiste = heapq.heappop(prJono)

                if matkaLahtopisteestaNyt > matka[lahtoPiste]:
                    continue

                for seuraavaKaupunki, hinta in self.junaYhteydet[lahtoPiste].items():
                    uusiMatka = matka[lahtoPiste] + hinta

                    if uusiMatka < matka[seuraavaKaupunki]:
                        matka[seuraavaKaupunki] = uusiMatka
                        edellinen[seuraavaKaupunki] = lahtoPiste
                        heapq.heappush(prJono, (uusiMatka, seuraavaKaupunki))

            rivi = [lahtoKaupunki]
            for pääteKaupunki in jarjKaupungit:
                rivi.append(matka[pääteKaupunki] if matka[pääteKaupunki] != float('inf') else -1)

            halvimmatReitit.append(rivi)

        return halvimmatReitit
if __name__ == "__main__":
    t = TrainPrices()
    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)



    l = t.find_prices()
    for rivi in l:
        print(rivi)
