
#  Time complexity: O(m+n + nlogn)

#  Space complexity: O(n) or O(logn)


from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        extra=[]

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    ans.append(arr1[j])
        
        for j in range(len(arr1)):
            if arr1[j] not in arr2:
                extra.append(arr1[j])
        
        extra.sort()
        return ans+extra
        
arr1=[2,3,1,3,2,4,6,7,9,2,19]
arr2=[2,1,4,3,9,6]
ans = Solution().relativeSortArray(arr1=arr1,arr2=arr2)     
print(ans)