class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n < 0:
        #     n = -n
        #     x = 1/x
        # if n == 0:
        #     return 1
        # else:
        #     res = 1
        #     while n > 0:
        #         if n % 2:
        #             res *= x
        #         x *= x
        #         n //= 2
        #     return res
        def fn(base, expo):
            if expo == 0:
                return 1
            elif expo % 2:
                return base * fn(base*base, (expo-1)//2)
            else:
                return fn(base*base, expo//2)
        res = fn(x, abs(n))
        return float(res) if n > 0 else 1/res
