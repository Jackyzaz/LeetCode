class Solution:
    def reverse(self, x: int) -> int:
        ans = str(x)
        i = -1
        # print(x)

        if len(str(x)) == 1:
            return x

        while ans[i] == '0':
            i-=1
    
        # print(i)
        # print(ans[:-2])
        # print(str(x).replace('-','')[i::-1])


        if x < 0:
            ans = '-'
            ans += (str(x).replace('-','')[i::-1])
        else :
            ans = ''
            ans += (str(x)[i::-1])

        if int(ans) > 2147483647 or int(ans) < -2147483648 :
            return 0


        return ans


awnser = Solution().reverse(x=1534236469)
print(awnser)