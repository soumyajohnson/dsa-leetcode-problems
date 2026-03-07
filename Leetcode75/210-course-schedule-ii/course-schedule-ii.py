class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        visited=set()
        finished=set()
        stack=[]
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
            stack.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return stack[::-1]