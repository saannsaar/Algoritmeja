

# def count(n, x):
    
#     # Helper function to check if the current arrangement is valid
#     def is_valid(arrangement):
#         for i in range(1, len(arrangement)):
#             if arrangement[i - 1] + arrangement[i] == arrangement[i + 1]:
#                 return False
#         return True

#     # Helper function for backtracking
#     def backtrack(arrangement):
#         count = 0
#         if len(arrangement) == n:
#             if is_valid(arrangement):
#                 count += 1
#             return

#         for num in range(1, n + 1):
#             if num not in arrangement:
#                 arrangement.append(num)
#                 backtrack(arrangement)
#                 arrangement.pop()
#         count = 0
#         starting_arrangement = [x]
#         backtrack(starting_arrangement)
#         return count

    



# if __name__ == "__main__":
#     print(count(1, 1)) # 1
#     print(count(4, 2)) # 4
#     print(count(8, 5)) # 830



