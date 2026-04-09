class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        q=deque([(beginWord,1)])
        visited=set()
        while q:
            curr,l=q.popleft()
            if curr==endWord:
                return l
            for i in range(len(beginWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword=curr[:i]+c+curr[i+1:]
                    if newword not in visited and newword in wordList:
                        visited.add(newword)
                        q.append((newword,l+1))
        return 0