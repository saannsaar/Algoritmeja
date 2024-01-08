class MaxSet:
    
    def __init__(self, n):
        self.vanhempi = list(range(n + 1))  
        self.arvo = [0] * (n + 1)  
        self.joukonKoko = [1] * (n + 1)  
        self.maxJoukonKoko = 1  

    def find(self, etsittävä):
        if self.vanhempi[etsittävä] != etsittävä:
            self.vanhempi[etsittävä] = self.find(self.vanhempi[etsittävä])
        return self.vanhempi[etsittävä]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.arvo[a] > self.arvo[b]:
                a, b = b, a
            self.vanhempi[a] = b
            self.joukonKoko[b] += self.joukonKoko[a]

            self.maxJoukonKoko = max(self.maxJoukonKoko, self.joukonKoko[b])
            if self.arvo[a] == self.arvo[b]:
                self.arvo[b] += 1

    def get_max(self):
        return self.maxJoukonKoko


if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max()) # 3
    m.merge(1, 5)
    print(m.get_max()) # 5
