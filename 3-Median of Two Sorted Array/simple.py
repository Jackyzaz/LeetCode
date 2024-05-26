from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeArray = nums1+nums2
        mergeArray.sort()
        n = len(mergeArray)
        if n % 2 == 1:
            return mergeArray[n//2]
        else :
            return (mergeArray[n//2]+mergeArray[(n//2)-1])/2
    
ans = Solution().findMedianSortedArrays(nums1=[1,2],nums2=[3,4])
print(ans)