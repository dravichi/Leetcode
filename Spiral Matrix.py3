class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row, col = len(matrix), len(matrix[0])
        t, b, l, r = 0, row-1, 0, col-1
        res = []
        while len(res) != row * col:
            for i in range(l, r+1):
                res.append(m[t][i])
            t += 1
            for i in range(t, b+1):
                res.append(m[i][r])
            r -= 1
            for i in range(r, l-1, -1):
                res.append(m[b][i])
            b += 1
            for i in range(b, t-1, -1):
                res.append(m[i][l])
        return res
