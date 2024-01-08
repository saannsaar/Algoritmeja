def create(n):
    nums = list(range(1, n+1))
    print(nums)
    print(len(nums))
    result = [1]
    for i in range(0,len(nums)):
        if nums[i] % 2 == 0:
            result.append(nums[i])
        else: 
            result = [nums[i]] + result
    return result



if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # None
    print(create(4)) # [2, 4, 1, 3]
    print(create(7)) # [1, 3, 5, 2, 6, 4, 7]
    print(create(10))