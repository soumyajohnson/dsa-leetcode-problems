class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        visited=set()
        finished=set()
        def dfs(i):
            if i in finished:
                return True
            if i in visited:
                return False
            visited.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            finished.add(i)
            visited.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True