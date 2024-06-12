# BruteForce Way 
# Runtime 3838 ms

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i != j ):
                # Debug Summation
                # print(f" [{i}] {nums[i]} : [{j}] {nums[j]} sum = {nums[i] + nums[j]}")
                if nums[i] + nums[j] == target :
                    return [i,j]
                
result = twoSum(nums=[3,2,4],target=6)
print(result)
