from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxLength = 0
        for s in sentences:
            ans = s.split(' ')
            maxLength = max(maxLength,len(ans))
        return maxLength