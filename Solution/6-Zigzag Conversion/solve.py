class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i=0
        j=0
        ans= [[]*numRows for i in range(numRows)]
        print(ans)
        for c in s:
            if numRows != 2:
                if j >= numRows-2:
                    i = 0
                    j = 0
                
                if i < numRows:
                    ans[i].append(c) 
                    print(i,c)
                    i+=1
                elif j < numRows-2:
                    ans[((-1)*j)+numRows-2].append(c) 
                    print(((-1)*j)+numRows-2,c)
                    j+=1
            else :
                if i < numRows:
                    ans[i].append(c) 
                    print(i,c)
                    i+=1
                    if i >= numRows:
                        i=0
        print(ans)
        print(''.join([x for xs in ans for x in xs]))
                


Solution().convert(s="ABC", numRows=2)