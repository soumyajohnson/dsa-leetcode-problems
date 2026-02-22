from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsmap=defaultdict()
        for i in range(len(nums)):
            if nums[i] in numsmap :
                if abs(numsmap[nums[i]]-i)<=k:
                    return True
            numsmap[nums[i]]=i
        return False