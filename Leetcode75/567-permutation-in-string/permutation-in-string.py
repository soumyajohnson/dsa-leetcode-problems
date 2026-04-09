class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        k=len(s1)-1
        l=0
        for r in range(k,len(s2)):
            if c1==Counter(s2[l:r+1]):
                return True
            l+=1
        return False