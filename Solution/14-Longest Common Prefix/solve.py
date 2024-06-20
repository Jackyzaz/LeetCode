# Verticle Search
# Time : O(n*m)
# Space : O(1)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):
            temp=strs[0][i]
            for j in range(1,len(strs)):
                # print(strs[j][i])
                if i == len(strs[j]) or strs[j][i] != temp :
                    return strs[0][0:i]

        return strs[0]




print(Solution().longestCommonPrefix(strs=["flower","flowe","flower"]))