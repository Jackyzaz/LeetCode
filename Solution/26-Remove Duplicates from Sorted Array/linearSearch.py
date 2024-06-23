# Bad Search Approch

# Time Comp: O(n^2)
# Mem Comp: O(n)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
            else:
                nums[i] = '_'

        while '_' in nums:
            nums.remove('_')
        print(nums)
        
        return len(nums)
    
print(Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))