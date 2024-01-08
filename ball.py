class Ball:
    def __init__(self, n):
        self.n = n
        self.verkko = [[0]*(2*n + 2) for _ in range(2*n + 2)]

    def add_pair(self, a, b):
        self.verkko[a][b + self.n] = 1
        self.verkko[0][a] = 1
        self.verkko[b + self.n][-1] = 1

    def leveyshaku(self, a, b, flow):
        if a in self.nahty:
            return 0
        self.nahty.add(a) 
        if a == b:
            return flow
        for x in range(len(self.verkko)):
            if self.virtaus[a][x] > 0:
                inc = self.leveyshaku(x, b, min(flow, self.virtaus[a][x]))
                if inc > 0:
                    self.virtaus[a][x] -= inc
                    self.virtaus[x][a] += inc
                    return inc
        return 0

    def calculate(self):
        self.nahty = None
        self.virtaus = None
        self.virtaus = [row[:] for row in self.verkko]
        total = 0
        while True:
            self.nahty = set()
            add = self.leveyshaku(0, len(self.verkko)-1, float('inf'))
            if add == 0:
                return total
            total += add


if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2