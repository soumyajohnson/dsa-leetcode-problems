class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        amap=defaultdict(set)
        adjmap=defaultdict(list)
        indegree=[0]*n
        for e in edges:
            adjmap[e[0]].append(e[1])
            indegree[e[1]]+=1
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        while q:
            u=q.popleft()
            print(q)
            for v in adjmap[u]:
                amap[v].add(u)
                amap[v].update(amap[u])
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        res=[]
        for i in range (n):
            res.append(sorted(amap[i]))
        return res