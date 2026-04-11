class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp=Counter(p)
        l=0
        res=[]
        for r in range(len(p)-1,len(s)):
            cs=Counter(s[l:r+1])
            if cs==cp:
                res.append(l)
            l+=1
        return res