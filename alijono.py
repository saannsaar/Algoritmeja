# Käytin apuna tätä sivua:
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/


import random


def lis(lista):
   n =len(lista)

   lis = [1]*n
   

   for i in range(1,n):
       for e in range (0, i):
           if lista[i] > lista[e] and lis[i] < lis[e] + 1:
               lis[i] = lis[e]+1
    
   maxpituus = 0
   
   for k in range(n): 
       maxpituus = max(maxpituus, lis[k])
    
   return maxpituus


def lista(p):
   
    alist = list(range(1, p+1))
    random.shuffle(alist)
    print(alist)
    return lis(alist)

print(lista(5000))

