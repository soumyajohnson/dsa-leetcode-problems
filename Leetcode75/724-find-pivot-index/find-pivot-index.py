class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        l,r=0,0
        for i,n in enumerate(nums):
            r=total-l-n
            if l==r:
                return i
            l+=n
        return -1