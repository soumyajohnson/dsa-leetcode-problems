class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for i in range(len(equations)):
            x=equations[i][0]
            y=equations[i][1]
            graph[x].append([y, values[i]])
            graph[y].append([x,1/ values[i]])
        res=[]
        def dfs(u, prod, v, visited):
            if u not in graph or v not in graph:
                return -1.0
            if u==v:
                return prod
            visited.add(u)
            for n,w in graph[u]:
                if n not in visited:
                    ans= dfs(n,prod*w,v,visited)
                    if ans!=-1:
                        return ans
            return -1
        for u,v in queries:
            res.append(dfs(u,1,v,set()))
        return res


            