class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for i in s:
            map1[i]=1+map1.get(i,0)
        for i in t:
            map2[i]=1+map2.get(i,0)
        if map1==map2:
            return True
        else:
            return False
