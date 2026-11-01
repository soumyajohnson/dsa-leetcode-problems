class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res=[]
        def dfs(path):
            if path[-1]==len(graph)-1:
                res.append(path)
            else:
                for child in graph[path[-1]]:
                    dfs(path+[child])
        dfs([0])
        return res