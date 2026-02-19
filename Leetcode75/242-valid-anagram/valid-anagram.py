from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        smap=defaultdict(int)
        tmap=defaultdict(int)
        for c1,c2 in zip(s,t):
            smap[c1]+=1
            tmap[c2]+=1
        return smap==tmap