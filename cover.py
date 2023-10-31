def count(n, m, k):
    if (k == 1):
        return 1
    else:
        return count(n-k, m, k-1) + count(n, m-k, k-1)

def cover(n, m, k):
    return count (n, m, k)

if __name__ == "__main__":
    print(cover(2,2,4)) # 8
    print(cover(2,3,3)) # 13
    print(count(4,4,1)) # 1
    print(cover(4,3,10)) # 3146
    print(count(4,4,16)) # 70878