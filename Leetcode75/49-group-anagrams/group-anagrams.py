class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap=defaultdict(list)
        for s in strs:
            strmap[''.join(sorted(s))].append(s)
        return list(strmap.values())