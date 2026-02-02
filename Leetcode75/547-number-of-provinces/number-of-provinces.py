class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        n=len(isConnected)
        visited=[False]*n
        count=0
        def dfs(i):
            for j in range(n):
                if visited[j]==False and isConnected[i][j]==1:
                    visited[j]=True
                    dfs(j)
        for i in range(n):
            if visited[i]==False:
                count+=1
                visited[i]=True
                dfs(i)
        
        return count
                