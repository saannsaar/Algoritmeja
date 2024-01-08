class Airports:
    def __init__(self, n):
        self.n = n
        self.yhteydet = {i: [] for i in range(1, n + 1)}

    def add_link(self, a, b):
       self.yhteydet[a].append(b)

    def check(self):
        n = len(self.yhteydet)

        for lähtöAsema in range(1, n + 1):
            käyty = set()
            pino = [lähtöAsema]

            while pino:
                
                asemaJossaOllaan = pino.pop()
                käyty.add(asemaJossaOllaan)
                # Lisätään viereiset pinoon jos niissä ei ole vielä käyty
                pino.extend(naapuri for naapuri in self.yhteydet[asemaJossaOllaan] if naapuri not in käyty)

            if len(käyty) != n:
                return False  

        return True
if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check())  # False
    print(a.yhteydet)
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check())  # False
    a.add_link(5, 1)
    print(a.yhteydet)
    print(a.check())  # True

