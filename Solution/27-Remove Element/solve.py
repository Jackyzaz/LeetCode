class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ans=[]
        for i in range(len(nums)):
            if nums[i] != val:
                ans.append(nums[i])
            
        while val in nums:
            nums.remove(val)
        print(nums)
        
        return len(ans)
    


print(Solution().removeElement(nums=[0,1,2,2,3,0,4,2],val=2))