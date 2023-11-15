class Solution:
    def myAtoi(self, s: str) -> int:
        s, n, res = s.lstrip(), 1, 0
        if s and s[0] == '+':
            s = s.removeprefix('+')
        elif s and s[0] == '-':
            s = s.removeprefix('-')
            n = -1
        if not s or not s[0].isdigit():
            return 0
        for i in range(len(s)):
            if s[i].isdigit():
                res = res*10 + int(s[i])
            else:
                break
        res *= n
        return 2147483647 if res > 2147483647 else -2147483648 if res < -2147483648 else res
