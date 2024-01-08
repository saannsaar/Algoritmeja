def count(n):
    if n == 1:
        return 1  # The original order is already restored for n=1
    steps = n - 1 if n % 2 == 1 else 2 ** (n.bit_length() - 1)
    return steps

if __name__ == "__main__":
    print(count(2)) # 2
    print(count(5)) # 6
    print(count(31)) # 240
    print(count(1234567)) # 381038919372