class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]*len(candies)
        maxc=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxc:
                res.append(True)
            else:
                res.append(False)
        return res
