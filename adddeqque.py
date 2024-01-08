from collections import deque
import time




def addTo(n):
    newD = deque()
    for i in range(1, n+1):
        newD.append(i)
    return newD

def deleteFrom(deq, n):
    for i in range(1, n+1):
        deq.pop()
    return deq

start = time.time()
addTo(100)
end = time.time()

print(end - start)


l = addTo(10000)
start = time.time()
deleteFrom(l, 10000)
end = time.time()
end = time.time()

print(end - start)



