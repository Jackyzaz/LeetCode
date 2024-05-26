from typing import List

class Solution:
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            print("🐍 | Line: 34 | findLengthOfLCIS2 ~ i",i)
            if i and nums[i-1] >= nums[i]: anchor = i
            print("🐍 | Line: 35 | findLengthOfLCIS2 ~ anchor",anchor)
            ans = max(ans, i - anchor + 1)
            print("🐍 | Line: 36 | findLengthOfLCIS2 ~ ans",ans)
            
        return ans
ans = Solution().findLengthOfLCIS2(nums=[1,3,5,4,2,3,4])
print('ans:',ans)    