class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def start():
            l,h=0,len(nums)-1
            res=-1
            while l<=h:
                mid=(l+h)//2
                if nums[mid]==target:
                    res=mid
                if nums[mid]>=target:
                    h=mid-1
                else:
                    l=mid+1
            return res
        def end():
            l,h=0,len(nums)-1
            res=-1
            while l<=h:
                mid=(l+h)//2
                if nums[mid]==target:
                    res=mid
                if nums[mid]<=target:
                    l=mid+1
                else:
                    h=mid-1
            return res
        return [start(),end()]
