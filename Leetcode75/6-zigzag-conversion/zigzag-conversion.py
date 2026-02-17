class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res=[""]*numRows
        down=1
        j=0
        for c in s:
            res[j]+=c
            if j==0:
                down=1
            elif j==numRows-1:
                down=-1
            j+=down
        ans=""
        for w in res:
            ans+=w
        return ans