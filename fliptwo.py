from collections import deque

def solve(n,k):
   
    dequeLista = deque(range(1, n + 1))

    for _ in range(k):
        if len(dequeLista) >= 2:
            elem1 = dequeLista.popleft()
            elem2 = dequeLista.popleft()

            dequeLista.append(elem2)
            dequeLista.append(elem1)
    return dequeLista.popleft()




if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875