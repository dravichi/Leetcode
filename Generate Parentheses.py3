class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generator(s, l , r):
            if n*2 == len(s):
                res.append(s)
                return
            if l > r:
                generator(s+")", l, r+1)
            if l < n:
                generator(s+"(", l+1, r)
        generator('(', 1, 0)
        return res
