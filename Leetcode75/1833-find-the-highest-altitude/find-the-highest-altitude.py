class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxalt= 0
        curalt=0
        for g in gain:
            curalt+=g
            maxalt=max(maxalt,curalt)
        return maxalt

