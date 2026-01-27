class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[]
        a0,a1=[],[]
        for n in nums1:
            if n not in nums2 and n not in a0:
                a0.append(n)
        answer.append(a0)
        for n in nums2:
            if n not in nums1 and n not in a1:
                a1.append(n)
        answer.append(a1)
        return answer