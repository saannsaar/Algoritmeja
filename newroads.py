import heapq

class NewRoads:
    def __init__(self, n):
        self.n = n
        self.tiet = []

    def find(self, kaupunki):
        if self.vanhemmat[kaupunki] != kaupunki:
            self.vanhemmat[kaupunki] = self.find(self.vanhemmat[kaupunki])
        return self.vanhemmat[kaupunki]

    def add_road(self, a, b, x):
        heapq.heappush(self.tiet, (x, a, b))
        

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.arvo[a] > self.arvo[b]:
            a, b = b, a
        self.vanhemmat[a] = b
        self.arvo[b] += self.arvo[a]
        
    
    def min_cost(self):
        self.vanhemmat = {x: x for x in range(1, self.n + 1)}
        self.arvo = {x: 0 for x in range(1, self.n + 1)}

        maksaa = 0
        tiet = self.tiet.copy()
        while tiet:
            x, a, b = heapq.heappop(tiet)
            if self.find(a) != self.find(b):
                maksaa += x
                self.union(a, b)

        #Tsekataan komponenttien määrä niin että jos solmu ja sen vanhempi on samat (key == value) eli ei ole tietä 
        # niiden välillä, ja niitä on enemmän kuin yksi 
        # on sillon kaupungissa yli 1 komponenttia ja haluttu määrä on 1 koska tarkoitus on muodostaa tieverkosto jossa kaikkiin kaupunkeihin
        # pääsee kulkemaan 
        if sum(key == value for key, value in self.vanhemmat.items()) > 1:
            return -1
        
        return maksaa



if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1, 2, 2)
    n.add_road(1, 3, 5)
    print(n.min_cost())  # -1
    n.add_road(3, 4, 4)
    print(n.min_cost())  # 11
    n.add_road(2, 3, 1)
    print(n.min_cost())  # 7