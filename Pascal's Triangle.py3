class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 0:
            return []
        for i in range(1, numRows):
            prev, temp = res[i-1], [1]
            for j in range(1, i):
                temp.append(prev[j-1] + prev[j])
            res.append(temp+[1])
        return res
