class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for f in c.values():
            if f>=2:
                return True
        return False