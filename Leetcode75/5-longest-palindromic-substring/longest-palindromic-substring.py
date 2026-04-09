class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo={}
        max_len=1
        max_start=0
        for i in range(len(s)):
            memo[(i,i)]=True
        def dfs(i,j):
            if i>=j:
                return True
            if s[i]!=s[j]:
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=dfs(i+1,j-1)
            return memo[(i,j)]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dfs(i,j):
                    if j-i+1>max_len:
                        max_len=j-i+1
                        max_start=i
        return s[max_start:max_start+max_len]