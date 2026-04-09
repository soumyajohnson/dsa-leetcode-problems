class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        visited=set()
        finished=set()
        res=[]
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
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]