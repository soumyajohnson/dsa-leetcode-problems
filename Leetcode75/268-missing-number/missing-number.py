class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        numset=set(nums)
        for i in range(n+1):
            if i not in numset:
                return i