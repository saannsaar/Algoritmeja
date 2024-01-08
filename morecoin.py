# def count(x, coins):
#     # Initialize a list to store the minimum number of coins needed for each value from 0 to x
#     dp = [float('inf')] * (x + 1)

#     # Base case: 0 coins needed for sum 0
#     dp[0] = 0

#     # Define the coin values
    

#     # Populate the dp table iteratively
#     for i in range(1, x + 1):
#         for coin in coins:
#             if i - coin >= 0:
#                 dp[i] = min(dp[i], dp[i - coin] + 1)

#     return dp[x] if dp[x] != float('inf') else -1

# if __name__ == "__main__":
#     print(count(5, [1])) # 1
#     print(count(5, [1, 2])) # 3
#     print(count(13, [1, 2, 5])) # 14
#     print(count(42, [1, 5, 6, 17])) # 58
#     print(count(99, [2, 4, 6])) # 0

def min_coins_for_sum_range(x):
    coins = [1, 4, 5]

    # Initialize a list to store the minimum number of coins needed for each value from 0 to x
    dp = [float('inf')] * (x + 1)

    # Base case: 0 coins needed for sum 0
    dp[0] = 0

    # Populate the dp table iteratively
    for coin in coins:
        for i in range(coin, x + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[x] if dp[x] != float('inf') else -1

def min_coins_for_sum_large(x):
    # Split the problem into smaller ranges
    ranges = [10**9, 10**18, 10**27]  # Adjust as needed

    result = 0
    current_range = 0

    while x > 0:
        current_range = min(x, ranges[result])
        result += min_coins_for_sum_range(current_range)
        x -= current_range

    return result

# Example usage:
from sympy import Integer

x = Integer(1337**9)
result = min_coins_for_sum_large(x)
print(f"The minimum number of coins needed to form the sum {x} is {result}.")
