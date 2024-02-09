def isEqual(x):
    return x.count(x[0]) == len(x)

nums = list(map(int, input().split()))

if isEqual(nums):
    print(10000 + (nums[0] * 1000))
elif nums[0] == nums[1] or nums[0] == nums[2]:
    print(1000 + (nums[0] * 100))
elif nums[1] == nums[2]:
    print(1000 + (nums[1] * 100))
else:
    print(max(nums) * 100)
