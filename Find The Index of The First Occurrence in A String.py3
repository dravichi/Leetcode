class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # In-built
      
        return haystack.find(needle)

        # User-defined
      
        # h, n = len(haystack), len(needle)
        # for i in range(h-n+1):
        #     for j in range(n):
        #         if needle[j] != haystack[i+j]:
        #             break
        #         if j == n - 1:
        #             return i
        # return -1
