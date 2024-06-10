from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        checkArray=[]
        expectHeights = sorted(heights)
        
        n = len(heights)
        for i in range(n):
            if expectHeights[i] != heights[i] :
                checkArray.append(i)
        return len(checkArray)
        
print(Solution().heightChecker(heights=[1,1,4,2,1,3]))
