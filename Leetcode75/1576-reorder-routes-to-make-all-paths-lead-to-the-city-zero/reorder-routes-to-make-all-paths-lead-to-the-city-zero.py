from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours=defaultdict(list)
        connected=set()
        for u,v in connections:
            neighbours[u].append(v)
            neighbours[v].append(u)
            connected.add((u,v))
        
        def dfs(u):
            res=0
            for n in neighbours[u]:
                if n not in visited:
                    visited.add(n)
                    if (n,u) not in connected:
                        res+=1
                    res+=dfs(n)
            return res
        
        visited=set()
        visited.add(0)
        return dfs(0)