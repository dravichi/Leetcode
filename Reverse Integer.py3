class Solution:
    def reverse(self, x: int) -> int:
        mini, maxi = -2147483648, 2147483647
        res = 0
        while x != 0:
            res = res * 10 + (x % 10 if x > 0 else x % -10)
            x = math.trunc(x / 10)
            if res > maxi or res < mini:
                return 0
        return res
