class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxlen,l=0,0
        start=0
        for n in numset:
            if n-1 not in numset:
                start=n
                l=0
                while start in numset:
                    l+=1
                    start+=1
                maxlen=max(maxlen,l)
        return maxlen
        