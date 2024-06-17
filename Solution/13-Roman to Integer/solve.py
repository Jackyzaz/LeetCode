class Solution:
    def romanToInt(self, s: str) -> int:
        s+='_'
        ans=0
        for i in range(len(s)):

            #Check M
            if s[i] == 'M' and s[i-1] != 'C':
                ans+=1000

            #Check D
            if s[i] == 'D' and s[i-1] != 'C':
                ans+=500

            #Check C
            if s[i] == 'C' and s[i+1] == 'D':
                ans+=400
            elif s[i] == 'C' and s[i+1] == 'M':
                ans+=900
            elif s[i] == 'C' and s[i-1] != 'X':
                ans+=100

            #Check L
            if s[i] == 'L' and s[i-1] != 'X':
                ans+=50

            #Check X
            if s[i] == 'X' and s[i+1] == 'L':
                ans+=40
            elif s[i] == 'X' and s[i+1] == 'C':
                ans+=90
            elif s[i] == 'X' and s[i-1] != 'I':
                ans+=10
           
            #Check V
            if s[i] == 'V' and s[i-1] != 'I':
                ans+=5
            
            #Check I
            if s[i] == 'I' and s[i+1] == 'V':
                ans+=4
            elif s[i] == 'I' and s[i+1] == 'X':
                ans+=9
            elif s[i] == 'I':
                ans+=1
           

        print(ans)
        return ans   

Solution().romanToInt(s='CD')