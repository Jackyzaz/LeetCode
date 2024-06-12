def countPoints(rings: str) -> int:
    ringMap={str:list}

    count = 0
    for i in range(len(rings[::2])):
        ringMap[rings[1::2][i]] = [rings[::2][i]]
    
    for i in range(len(rings[::2])):
        if rings[::2][i] not in ringMap[rings[1::2][i]]:
            ringMap[rings[1::2][i]].append(rings[::2][i])
            print(ringMap)
            if len(ringMap[rings[1::2][i]]) == 3:
                count+=1
    
    return count

def countPoints2(rings: str) -> int:
    lst=[]
    rgb=[]
    count=0
    for i in range(1,len(rings),2):
        rgb=[]
        if rings[i] not in lst:
            lst.append(rings[i])
            for j in range(1,len(rings),2):
                if rings[j]==rings[i]:
                    if rings[j-1]=='R':
                        rgb.append(rings[j-1])
                    if rings[j-1]=='G':
                        rgb.append(rings[j-1])
                    if rings[j-1]=='B':
                        rgb.append(rings[j-1])
            if len(set(rgb))==3:
                count+=1
    return count
print(countPoints2(rings="G3R3R7B7R5B1G8G4B3G6"))
# print(countPoints(rings="B0B6G0R6R0R6G9"))