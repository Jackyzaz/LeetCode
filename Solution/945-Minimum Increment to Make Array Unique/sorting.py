# Sorting Algorithm
# Time complexity : O(nlogn)

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        n = len(nums)
        count=0

        nums.sort()
        print(nums)

        for i in range(1,n):
            if nums[i-1] < nums[i]:
                continue
            elif nums[i-1] == nums[i]:
                count+=1
                nums[i]+=1
            elif nums[i-1] > nums[i]:
                count+=(nums[i-1]-nums[i]+1)
                nums[i]=nums[i-1]+1

            
        # print(nums)

        # print(ans)
        return count

print(Solution().minIncrementForUnique(nums=[3,2,1,2,1,7]))