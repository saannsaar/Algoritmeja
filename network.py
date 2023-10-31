from collections import deque
from collections import defaultdict

class Network:

    def __init__(self,n):
        self.verkko = [[] for _ in range(n+1)]
       
    # Lisää yhteyden kahden tietokoneen välille
    def add_link(self,a,b):
        self.verkko[a].append(b)
        self.verkko[b].append(a)
        

    # Etsii suorimman reitin kahden koneen välillä
    def best_route(self, a, b):
        kayty = set()
        apulista = deque((solmu, 1) for solmu in self.verkko[a])
        print("QUEUE",apulista)
        while apulista:
            
            solmu, pituus = apulista.popleft()
            print(solmu, pituus)
            if solmu in kayty:
                continue
            # Löydettiin solmu mihin haluttiin päästä
            if solmu == b:
                return pituus
            #Lisätään käydyksi solmu missä ollaan
            kayty.add(solmu)
            apulista.extend((naapuri, pituus+1) for naapuri in self.verkko[solmu])
        return -1
               

if __name__ == "__main__":
    w = Network(5)
    print(w.verkko)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
   
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.verkko)
    print(w.best_route(1,5)) # 2

