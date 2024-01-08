import heapq


def smallest(n):

    # Käytetään kekoa koska isojen lukujen kanssa paljon helpompaa kun voidaan aina vaan poistaa ensimmäinen alkio koska
    # keossa jokainen arvo on vähemmän tai samanverran kun sen "lapsialkiot".
    # Alustetaan keko niin että siellä on luku 1. 
    heap = [1]

    # Luupataan n kierrosta
    for _ in range(n):
        # Poistetaan pienin alkio keosta eli eka
        smallest = heapq.heappop(heap)

        # Lisätään kekoon 2 * pienin ja 3 * pienin
        heapq.heappush(heap, 2 * smallest)
        heapq.heappush(heap, 3 * smallest)

    # Palautetaan pienin alkio n kierroksen jälkeen eli eka alkio
    return heap[0]


if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(7)) # 9
    print(smallest(10)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552