class Download:
    def __init__(self,n):
        self.solmut = range(1, n + 1)
        self.verkko = {}
        for i in self.solmut:
            for j in self.solmut:
                self.verkko[(i, j)] = 0

    def add_link(self, a, b):
        self.verkko[(a, b)] = 1

    def add_flow(self, solmu, sink, flow):
        if solmu in self.kayty:
            return 0
        self.kayty.add(solmu)
        if solmu == sink:
            return flow
        for seuraavaSolmu in self.solmut:
            print(seuraavaSolmu)
            if self.flow[(solmu, seuraavaSolmu)] > 0:
                uusiSolmu = min(flow, self.flow[(solmu, seuraavaSolmu)])
                inc = self.add_flow(seuraavaSolmu, sink, uusiSolmu)
                print(inc)
                if inc > 0:
                    self.flow[(solmu, seuraavaSolmu)] -= inc
                    self.flow[(seuraavaSolmu, solmu)] += inc
                    return inc
        return 0

    def calculate(self, a, b):
        self.flow = self.verkko.copy()
        maara = 0
        while True:
            self.kayty = set()
            lisaa = self.add_flow(a, b, float("inf"))
            if lisaa == 0:
                break
            maara += lisaa
        return maara
    

if __name__ == "__main__":
    d = Download(5)
    print(d.calculate(1, 5)) # 0
    d.add_link(1, 2)
    d.add_link(2, 5)
    # print(d.calculate(1, 5)) # 7
    print(d.verkko)
    d.add_link(1, 5)
    print(d.verkko)
    print(d.calculate(1, 4)) # 8