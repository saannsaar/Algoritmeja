import heapq

class Median:
    def __init__(self):
         # Alustetaan kaksi kekoa: isoKeko isommalle puolelle ja pieniKeko pienelle puolelle
        self.pieniKeko = []  
        self.isoKeko = []  

    def add(self, x):
        # Lisää luvun jompaan kumpaan kekoon
        if not self.isoKeko or x <= -self.isoKeko[0]:
            heapq.heappush(self.isoKeko, -x)
        else:
            heapq.heappush(self.pieniKeko, x)

        # Tasapainotetaan keot koska mediaanin laskua varten 
        # on tehokkaampaa määritellä kahden keskimmäisen keskiarvo jos kekojen erotus on max 1
        # Eli jos self.isoKeko:ssa on enemmän kuin yksi elementti enemmän kun self.pieniKeko:ssa, otetaan pienin
        # elementti self.isoKeko:sta ja lisätään sen elementin negaatio self.pieniKeko:on
        if len(self.isoKeko) > len(self.pieniKeko) + 1:
            heapq.heappush(self.pieniKeko, -heapq.heappop(self.isoKeko))
        elif len(self.pieniKeko) > len(self.isoKeko):
            heapq.heappush(self.isoKeko, -heapq.heappop(self.pieniKeko))

    def median(self):
        # Jos parillinen määrä
        if len(self.isoKeko) == len(self.pieniKeko):
            # Palauta ensimmäisistä elementeistä pienempi
            return min(-self.isoKeko[0], self.pieniKeko[0])
        else:
            # Jos lukuja on pariton määrä 
            return -self.isoKeko[0]


if __name__ == "__main__":
    m = Median()
    m.add(1)
    print(m.median()) # 1
    m.add(2)
    print(m.median()) # 1
    m.add(3)
    print(m.median()) # 2
    m.add(4)
    print(m.median()) # 2
    m.add(5)
    print(m.median()) # 3