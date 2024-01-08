import heapq
import random
import timeit
from collections import namedtuple


Edge = namedtuple("Edge", ["end", "weight"])

N = 5000
INF = 2 ** 63

import heapq

  
def find_distances(verkko, alku):
        matka = {i: 0 if i == alku else INF for i in range(1, N + 1)}
        kayty = set()
        jono = [(0, alku)]
        while jono:
            __, solmu = heapq.heappop(jono)
            if solmu in kayty:
                continue

            for kaari in verkko[solmu]:
                current = matka[kaari.end]
                new = matka[solmu] + kaari.weight
                if new < current:
                    matka[kaari.end] = new
                    heapq.heappush(jono, (new, kaari.end))

            kayty.add(solmu)
        return matka
    

if __name__ == "__main__":
    verkko = {
        a: [
            Edge(b, random.randint(1, 1000))
            for b in random.sample(range(1, N + 1), k=N) if a < b and b - a < 10
        ]
        for a in random.sample(range(1, N + 1), k=N)
    }
    start = timeit.default_timer()
    vastaus = find_distances(verkko, 1)
    end = timeit.default_timer()
    print(start, end)
    print(f"Aikaa meni: {end - start} sekuntia")