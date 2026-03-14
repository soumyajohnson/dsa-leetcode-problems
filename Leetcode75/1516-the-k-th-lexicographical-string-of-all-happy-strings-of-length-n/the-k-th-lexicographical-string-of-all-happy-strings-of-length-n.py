class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(curr):
            nonlocal k
            if len(curr)==n:
                k-=1
                if k==0:
                    return curr
                return
            for c in "abc":
                if not curr or curr[-1]!=c:
                    res=dfs(curr+c)
                    if res:
                        return res
        return dfs("") or ""
            