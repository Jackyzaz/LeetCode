# fail attempt cause Time Limit Exceeded

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        n = len(nums)
        ans=[]
        count=0

        for i in range(n):
            while nums[i] in ans:
                nums[i]+=1
                count+=1
            if nums[i] not in ans:
                ans.append(nums[i])
            

        print(ans)
        return count

print(Solution().minIncrementForUnique(nums=[3,2,1,2,1,7]))