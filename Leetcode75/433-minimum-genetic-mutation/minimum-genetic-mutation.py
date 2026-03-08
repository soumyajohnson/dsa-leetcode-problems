class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank=set(bank)
        visited=set()
        q=deque([(startGene,0)])
        while q:
            curr,l=q.popleft()
            if curr==endGene:
                return l
            for i in range(8):
                for c in "ACGT":
                    new_gene=curr[:i]+c+curr[i+1:]
                    if new_gene not in visited and new_gene in bank:
                        visited.add(new_gene)
                        q.append((new_gene,l+1))
        return -1