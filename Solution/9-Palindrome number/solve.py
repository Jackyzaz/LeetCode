class Solution:
    def isPalindrome(self, x: int) -> bool:
        xString = str(x)
        n = len(xString)
        if xString[0:(n//2)] == xString[n:(n//2)-1:-1] :
            return True
        elif xString[0:(n//2)] == xString[n:(n//2):-1] :
            return True
        else:
            return False

print(Solution().isPalindrome(x=1221))