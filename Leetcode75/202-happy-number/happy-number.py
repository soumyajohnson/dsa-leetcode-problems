class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True
        elif 1<n<=9:
            return False
        else:
            n0=0
            while n!=0:
                n0+=(n%10)**2
                n=n//10
            return self.isHappy(n0)