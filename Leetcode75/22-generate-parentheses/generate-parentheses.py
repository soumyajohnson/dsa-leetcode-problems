class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(curr,o,c):
            if o==c and c==n:
                res.append(curr)
                return
            if o<n:
                dfs(curr+'(',o+1,c)
            if c<o:
                dfs(curr+')',o,c+1)
        dfs("",0,0)
        return res
