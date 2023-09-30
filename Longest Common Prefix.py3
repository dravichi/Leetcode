class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        strs.sort()
        x, y = strs[0], strs[-1]
        for i in range(min(len(x), len(y))):
            if x[i] == y[i]:
                res += x[i]
            else:
                return res
        return res
        
