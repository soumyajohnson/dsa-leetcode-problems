class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n=0
        while a>0 or b>0 or c>0:
            ai=a&1
            bi=b&1
            ci=c&1
            if ci==1:
                if ai==0 and bi==0:
                    n+=1
            else:
                n+=ai+bi
            a>>=1
            b>>=1
            c>>=1
        return n
