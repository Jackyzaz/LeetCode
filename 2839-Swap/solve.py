def canBeEqualv1( s1: str, s2: str) -> bool:
        for i in (s1):
            if (i in s2) == False:
                return False
        arr1=list(s1)
        arr2=list(s2)
        if s1 == s2:
            return True
        else:
            temp = arr1[0]
            arr1[0] = arr1[2]
            arr1[2] = temp
            if arr1[0] == arr2[0] and arr1[2] == arr2[2]:
                return True
            else:
                arr1=list(s1)
                temp = arr1[1]
                arr1[1] = arr1[3]
                arr1[3] = temp
                if arr1[1] == arr2[1] and arr1[3] == arr2[3]:
                    return True
                else:
                    return False
                
def canBeEqualv2(s1: str, s2: str) -> bool:
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])

print(canBeEqualv2(s1='xyzd',s2='zyxd'))