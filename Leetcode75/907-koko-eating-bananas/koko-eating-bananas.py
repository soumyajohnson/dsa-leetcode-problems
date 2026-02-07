class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk=max(piles)
        l,r=1,maxk
        while l<=r:
            mid=(l+r)//2
            hours=0
            for p in piles:
                hours+=ceil(p/mid)
            if hours<=h:
                r=mid-1
            else:
                l=mid+1
        return l