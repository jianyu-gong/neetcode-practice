class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        row_hash_set = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        col_hash_set = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        square_hash_set = {(0,0): set(), (0,1): set(), (0,2): set(), (1,0): set(), (1,1): set(), (1,2): set(), (2,0): set(), (2,1): set(), (2,2): set()}


        for i in range(m):
            for j in range(n):
                # print(i//3, j//3, i, j)
                if board[i][j] == '.':
                    continue

                if (board[i][j] in row_hash_set[i]) or (board[i][j] in col_hash_set[j]) or (board[i][j] in square_hash_set[(i//3, j//3)]):
                    print(i,j)
                    print(row_hash_set[i], )
                    return False
                else:
                    row_hash_set[i].add(board[i][j])
                    col_hash_set[j].add(board[i][j])
                    square_hash_set[(i//3,j//3)].add(board[i][j])

        return True
        