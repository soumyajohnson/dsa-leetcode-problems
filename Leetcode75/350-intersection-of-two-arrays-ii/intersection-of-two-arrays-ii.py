class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            self.intersect(nums2,nums1)
        c=Counter(nums1)
        common=[]
        for n in nums2:
            if c[n]>0:
                common.append(n)
                c[n]-=1
        return common
        