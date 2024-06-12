from typing import List

def restoreString(s: str, indices: List[int]) -> str: 
    hashmap = {}
    for index,items in enumerate(indices):
        hashmap[items] = s[index]
        print("🐍 File: 1528-Shuffle String/hashmap.py | Line: 7 | restoreString ~ hashmap",hashmap)

    print(hashmap)

    indices.sort()

    res = ""

    for i in range(len(indices)):
        res = res + hashmap[indices[i]]
        print(i,hashmap[indices[i]])
        print("🐍 File: 1528-Shuffle String/hashmap.py | Line: 17 | restoreString ~ res",res)

    return res   

print(restoreString(s='codeleet',indices=[4,5,6,7,0,2,1,3]))