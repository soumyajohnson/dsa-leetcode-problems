from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        pairs=0
        for n in nums:
            if d[k-n]>0:
                pairs+=1
                d[k-n]-=1
            else:
                d[n]+=1
        return pairs
