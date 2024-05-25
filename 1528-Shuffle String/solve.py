from typing import List

def restoreString(s: str, indices: List[int]) -> str:
    ans = ""
    for i in range(len(s)):
        ans+=(s[indices.index(i)])
    return ans


print(restoreString(s="codeleet",indices=[4,5,6,7,0,2,1,3]))