class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp = res = 0
        d = dict()
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= temp:
                    temp = d[s[i]] + 1
            if i - temp + 1 > res:
                res = i-temp + 1
            d[s[i]] = i
        return res
