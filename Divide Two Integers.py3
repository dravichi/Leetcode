class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
      sign = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)
      dividend = abs(dividend)
      divisor = abs(divisor)
      res = len(range(divisor-1, dividend, divisor))
      if sign:
          res = -res
      return max(min(res, 2147483647), -2147483648)
