class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix=0
        prefixmap={0:-1}
        res=0
        for i,n in enumerate(nums):
            if n==0:
                prefix-=1
            else:
                prefix+=1
            if prefix in prefixmap:
                res=max(res,i-prefixmap[prefix])
            else:
                prefixmap[prefix]=i
        return res