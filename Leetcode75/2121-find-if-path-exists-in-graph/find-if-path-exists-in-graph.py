class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_map=defaultdict(list)
        for u,v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
        visited=set()
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for nei in adj_map[node]:
                if nei not in visited and dfs(nei):
                    return True
            return False
        return dfs(source)