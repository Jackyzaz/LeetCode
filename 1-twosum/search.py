# Search Way 
# Runtime 3257 ms

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
       for j in range(len(nums)):
          if nums[j] == (target-nums[i]) and j != i:
            return [i,j]
        # if (target - nums[i]) in nums:


        #     k = nums.index(target-nums[i])
        #     if k == i:
        #         k = (len(nums))+1
        #     else :
        #         return [i,k]


result = twoSum(nums=[3,2,3],target=6)
print(result)
