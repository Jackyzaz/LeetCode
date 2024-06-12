class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        nums=str(n)
        
        for i in range(len(nums)):
            ans+=pow(-1,i)*int(nums[i])

        return ans


Solution().alternateDigitSum(n=521)