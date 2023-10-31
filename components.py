from collections import deque



def laskekomponentit(verkko):
    komponentit = 0
    kayty = set()
    
    for solmu, viereiset in verkko.items():
        if solmu in kayty:
            continue

        queue = deque(viereiset)
        print(queue)
        while queue:
            vieres = queue.popleft()
            print(vieres)
            if vieres in kayty:
                continue

            kayty.add(vieres)
            print(kayty)
            queue.extend(verkko[vieres])

        komponentit += 1

    return komponentit


if __name__ == "__main__":
    verkko = {
        solmu: [solmu2 for solmu2 in range(2, 1000 + 1) 
            if solmu != solmu2 and (solmu % solmu2 == 0 or solmu2 % solmu == 0)]
            for solmu in range(2, 1000 + 1)
    }
   
    print(verkko)
    print("VASTAUS: ",laskekomponentit(verkko))