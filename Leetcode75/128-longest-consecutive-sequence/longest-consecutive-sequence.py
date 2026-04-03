class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for n in nums:
            if n-1 not in nums:
                start=n
                l=1
                while start+1 in nums:
                    l+=1
                    start+=1
                longest=max(longest,l)
        return longest