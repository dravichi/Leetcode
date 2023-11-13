class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        def palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)-1):
            odd = palindrome(i, i)
            even = palindrome(i, i+1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res
