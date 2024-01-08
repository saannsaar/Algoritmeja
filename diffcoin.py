
def count(amount, coins):
        dyPo =  [0] * (amount+1)
        dyPo[0] = 1
        for i in range(0, len(coins)):
          for x in range(coins[i], amount +1):
                dyPo[x] += dyPo[x - coins[i]]
        return dyPo[amount]


if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2])) # 3
    print(count(13, [1, 2, 5])) # 14
