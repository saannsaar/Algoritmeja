#Lista sisältää kokonaisluvut 1 \dots n. Monellako tavalla voit valita listalta k lukua niin, että niiden summa on x?

#Voit olettaa, että 1 \le n \le 10 ja 1 \le k \le n. Algoritmisi tulee toimia tehokkaasti kaikissa näissä tapauksissa.

from itertools import combinations

def count(n, k, x):
   
    if n == 1:
        return n
    createList = list(range(1, n +1))


    l = 0
    # Ei paras mahdollinen toteutus jos käsiteltävänä isoja lukuja 
    for combination in combinations(createList, k):
        if sum(combination) == x:
            l = l + 1
    return l


if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16