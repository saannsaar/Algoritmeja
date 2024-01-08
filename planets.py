

class Planets:
    def __init__(self,n):
        self.planeetat = range(1, n + 1)
        self.verkko = {}
        for i in self.planeetat:
            for j in self.planeetat:
                self.verkko[(i, j)] = 0

    def add_teleport(self, a, b):
        capacity = 1
        self.verkko[(a, b)] += capacity

    def lisaaVirtaus(self, teleportti, paattyy, virtaus):
        if teleportti in self.kayty:
            return 0
        self.kayty.add(teleportti)
        if teleportti == paattyy:
            return virtaus
        for seuraavaTeleportti in self.planeetat:
            if self.virtaus[(teleportti, seuraavaTeleportti)] > 0:
                uusiVirtaus = min(virtaus, self.virtaus[(teleportti, seuraavaTeleportti)])
                inc = self.lisaaVirtaus(seuraavaTeleportti, paattyy, uusiVirtaus)
                if inc > 0:
                    self.virtaus[(teleportti, seuraavaTeleportti)] -= inc
                    self.virtaus[(seuraavaTeleportti, teleportti)] += inc
                    return inc
        return 0

    def calculate(self):
        lahto = 1
       
        paattyy = len(self.planeetat)
        self.virtaus = self.verkko.copy()
        total = 0
        while True:
            self.kayty = set()
            lisaa = self.lisaaVirtaus(lahto, paattyy, float("inf"))
            if lisaa == 0:
                break
            total += lisaa
        return total
    
if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate())  # Output: 0
    p.add_teleport(1, 2)
    p.add_teleport(2, 5)
    print(p.calculate())  # Output: 1
    p.add_teleport(1, 5)
    print(p.calculate())  # Output: 2
