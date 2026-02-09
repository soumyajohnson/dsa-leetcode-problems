class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(start,k,n,comb):
            if k==0 and n==0:
                res.append(comb.copy())
                return
            for i in range(start,10):
                if k==0 or n<=0:
                    break
                comb.append(i)
                dfs(i+1,k-1,n-i,comb)
                comb.pop()
        dfs(1,k,n,[])
        return res
            