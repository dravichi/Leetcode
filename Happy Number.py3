class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in check:
                return False
            check.add(n)
        return True
