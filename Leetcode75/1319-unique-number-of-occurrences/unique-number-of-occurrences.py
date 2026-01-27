class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrmap={}
        for a in arr:
            arrmap[a]=arrmap.get(a,0)+1
        return len(arrmap)==len(set(arrmap.values()))