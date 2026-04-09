class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(n) for n in nums]
        from functools import cmp_to_key
        def compare(x,y):
            if x+y>y+x:
                return -1
            else:
                return 1
        nums.sort(key=cmp_to_key(compare))
        if nums[0]=="0":
            return "0"
        return ''.join(nums)