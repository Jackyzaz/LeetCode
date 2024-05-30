class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        palindLength = 0

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print('line 9  |',i,j)
                print('line 10 |',s[i],s[j])
                if s[i] == s[j] and self.checkPalindome(s[i:j+1]):
                    if j - i > palindLength:
                        ans=s[i:j+1]
                        print("🐍 File: 5-Longest Palindromic Substring/solve.py | Line: 12 | longestPalindrome ~ ans",ans)
                        palindLength = j-i
                print()
                
        if ans == '':
            return s[0]

        return ans
    
    def checkPalindome(self, s:str) -> str:
        
        n = len(s)
        print(n)
        # print(n//2)

        print('line 35 |',s[0:(n//2)])
        print('line 35 |',s[n-1:(n//2)-1:-1])

        if s[0:(n//2)] == s[n:(n//2):-1]:
            return True  
        elif s[0:(n//2)] == s[n:(n//2)-1:-1]:
            return True
        else :
            return False


# print(Solution().checkPalindome(s='baaaab'))
# print('abcbab'[0:2])

anwser = Solution().longestPalindrome(s='ac')
print('anwser',anwser)