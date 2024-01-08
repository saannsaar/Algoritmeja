import heapq
INF = 2 ** 63
from collections import namedtuple

Edge = namedtuple("Edge", ["loppu", "paino"])

class BestRoute:
    def __init__(self, n):
        self.verkko =  {i: [] for i in range(1, n + 1)}
        self.n = n 

    def add_road(self, a, b, x):
        self.verkko[a].append(Edge(b, x))
        self.verkko[b].append(Edge(a, x))


    def find_route(self, a, b):
            # Alustetaan rakenne johon tallennetaan sitten lyhyimmät reitit jokaiseen kaupunkiin
            lyhyimmatMatkat = {i: 0 if i == a else INF for i in range(1, self.n + 1)}
            # Taulukko jossa pidetään tietoja siitä missä kaupungeissa jo käyty
            kayty = set()
            # Prioriteettijono alustetaan aloituskapungilla
            jono = [(0, a)]
            # Loopataan kaikki jonossa olevat kaupungit
            while jono:
                # Kaupunki jolla lyhyin reitti atm
                __, solmu = heapq.heappop(jono)
                #Jos kaupungissa käyty, skippaa
                if solmu in kayty:
                    continue
                kayty.add(solmu)
                for naapuri in self.verkko[solmu]:
                    # Laske mahdollinen lyhyin reitti naapuriin
                    nykyinen = lyhyimmatMatkat[naapuri.loppu]
                    uusi = lyhyimmatMatkat[solmu] + naapuri.paino
                    # Jos laskettu matka on lyhyempi kun nykynen lyhyin, päivitä
                    if uusi < nykyinen:
                        lyhyimmatMatkat[naapuri.loppu] = uusi
                        heapq.heappush(jono, (uusi, naapuri.loppu))

             # Jos ei löydy reittiä, palauta -1, muuten palauta lyhyin reitti
            return lyhyimmatMatkat[b] if b in kayty else -1

if __name__ == "__main__":
    b = BestRoute(5)
    b.add_road(4,5,4)
    print(b.find_route(3,4)) # -1
    b.add_road(4,5,9)
    print(b.find_route(3,5)) # -1
    print(b.find_route(1,5)) # -1
    b.add_road(1,4,5)
    print(b.find_route(1,4)) # 5
    b.add_road(3,4,7)
    b.add_road(2,3,1)
    print(b.find_route(2,5)) 
