class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        s = s[::-1]
        temp = 'I'
        for v in s:
            if d[v] < d[temp]:
                res -= d[v]
            else:
                res += d[v]
            temp = v
        return res
