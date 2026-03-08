class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        visited=set()
        if endWord not in wordList:
            return 0
        q=deque([(beginWord,1)])
        while q:
            curr,l=q.popleft()
            if curr==endWord:
                return l
            for i in range(len(beginWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_gene=curr[:i]+c+curr[i+1:]
                    if new_gene not in visited and new_gene in wordList:
                        visited.add(new_gene)
                        q.append((new_gene,l+1))
        return 0