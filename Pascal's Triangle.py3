class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1], [1, 1]]
        for i in range(3, numRows+1):
            temp = [1]
            for j in range(i-2):
                temp.append(a[i-2][j] + a[i-2][j+1])
            a.append(temp+[1])
        return a[:numRows]
