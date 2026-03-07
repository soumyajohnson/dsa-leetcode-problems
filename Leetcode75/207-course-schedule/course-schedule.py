from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        visited=set()
        finished=set()
        def dfs(node):
            if node in finished:
                return True
            if node in visited:
                return False
            visited.add(node)
            for v in graph[node]:
                if not dfs(v):
                    return False
            finished.add(node)
            visited.remove(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 