class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        def bs(s):
            idx=-1
            l,r=0,len(potions)-1
            while l<=r:
                mid=(l+r)//2
                if potions[mid]*s>=success:
                    idx=mid
                    r=mid-1
                else:
                    l=mid+1
            return idx
        for s in (spells):
            idx=bs(s)
            res.append(len(potions)-idx if idx!=-1 else 0)
        return res

