class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        n=len(isConnected)
        visited=set()
        count=0
        def dfs(i):
            for j in range(n):
                if j not in visited and isConnected[i][j]==1:
                    visited.add(j)
                    dfs(j)
        for i in range(n):
            if i not in visited :
                visited.add(i)
                dfs(i)
                count+=1
        return count