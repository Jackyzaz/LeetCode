class Solution:
    def myAtoi(self, s: str) -> int:
        numList='0123456789'
        n = len(s)
        elem=0
        symbol=''
        symelem=0
        ans = ''

        if len(s) == 0:
            return 0
        
        for i in range(n):
            if s[i] == " " :
                if elem ==0:
                    continue
                else:
                    if len(ans) == 0:
                        return 0
                    else :
                        return int(symbol+ans)
                    
            if ans == "" :
                if s[i] == "+" and elem==0:
                    symelem+=1
                    elem+=1
                    continue
                if s[i] == "-" and elem==0:
                    symelem+=1
                    symbol="-"
                    elem+=1
                    continue
                if s[i]== '0' :
                    elem+=1
                    continue

            if s[i] in numList and symelem <= 1 :
                ans+=s[i]
                elem+=1
            else:
                if len(ans)==0:
                    return 0 
                else:
                    if int(symbol+ans) < -2147483648:
                        return -2147483648
                    if int(symbol+ans) > 2147483647:
                        return 2147483647
                    else:
                        return int(symbol+ans)
                    
        if len(ans) == 0:
            return 0
        if int(symbol+ans) < -2147483648:
            return -2147483648
        if int(symbol+ans) > 2147483647:
            return 2147483647
        else:
            return int(symbol+ans)    
    
    
print(Solution().myAtoi(s="4193 with words"))    
# print(Solution().myAtoi(s="0-1"))    

