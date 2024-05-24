# Search Way 
# Runtime 56 ms

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
        print(i,numMap)


result = twoSum(nums=[2,1,11,7],target=9)
print(result)
