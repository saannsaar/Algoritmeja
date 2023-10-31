
def montatapaa(N, K):
    
    if N == 0:
        return 1
    if N < 0 or K <= 0:
        return 0
 
    return montatapaa(N - K, K) + montatapaa(N, K - 1)
 
def count(n):
    numero = n
    k = n
    return montatapaa(numero, k)

if __name__ == '__main__':
  
 
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174