class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def segment(i):
            if i==len(s):
                return True
            if i in memo:
                return memo[i]
            for j in range(i+1,len(s)+1):
                if s[i:j] in set(wordDict) and segment(j):
                    memo[i]=True
                    return True
            memo[i]=False
            return memo[i]
        return segment(0)
