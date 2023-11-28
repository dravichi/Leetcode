class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, sub= [set() for _ in range(9)], [set() for _ in range(9)], [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                rc = board[i][j]
                if rc != '.' and (rc in row[i] or rc in col[j] or rc in sub[i//3][j//3]):
                    return False
                row[i].add(rc)
                col[j].add(rc)
                sub[i//3][j//3].add(rc)
        return True
