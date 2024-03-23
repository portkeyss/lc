class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                res += 1
        return res