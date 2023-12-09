class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            temp = ''.join(sorted(i))
            d[temp] = d.get(temp, []) + [i]
        return d.values()
