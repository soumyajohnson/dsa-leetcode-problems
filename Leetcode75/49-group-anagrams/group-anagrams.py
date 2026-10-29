class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if strs is None or len(strs)==1:
            return [strs]
        ann_map=defaultdict(list)
        for s in strs:
            sorted_str="".join(sorted(s))
            ann_map[sorted_str].append(s)
        return list(ann_map.values())
            