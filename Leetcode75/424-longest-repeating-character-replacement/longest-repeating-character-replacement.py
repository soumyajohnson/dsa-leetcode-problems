class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        max_freq=0
        max_len=0
        l,r=0,0
        for r in range(len(s)):
            freq[s[r]]+=1
            max_freq=max(max_freq,freq[s[r]])
            while (r-l+1)-max_freq>k:
                freq[s[l]]-=1
                l+=1
            max_len=max((r-l+1),max_len)
        return max_len