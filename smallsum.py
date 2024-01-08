def find(n):
   # Handle base case
    if n == 1:
        return 0

    result = 0
    while n > 1:
        msb_position = 0
        temp = n
        while temp > 0:
            msb_position += 1
            temp >>= 1

        result += 2**(msb_position - 2) * (n - 2**(msb_position - 1) + 1)
        n = 2**(msb_position - 1) - 1

    return result

if __name__ == "__main__":
    print(find(1)) # 0
    print(find(2)) # 1
    print(find(3)) # 2
    print(find(4)) # 3
    print(find(5)) # 3
    print(find(123)) # 15
    print(find(123456)) # 62