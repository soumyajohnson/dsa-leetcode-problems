class Solution:
    def mySqrt(self, x: int) -> int:
        l,h=0,x
        ans=0
        while l<=h:
            mid=(l+h)//2
            mid_sqr=mid*mid
            if mid_sqr==x:
                return mid
            elif mid_sqr>x:
                h=mid-1
            else:
                ans=mid
                l=mid+1
        return ans
        