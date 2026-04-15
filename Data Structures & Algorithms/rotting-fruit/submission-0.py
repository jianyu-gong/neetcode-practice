class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        fresh_orange = 0
        res = 0

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 2:
                    queue.append((r, c))

                if grid[r][c] == 1:
                    fresh_orange += 1

        print(f'{fresh_orange=}')
        
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]

        while queue and fresh_orange > 0:
            for i in range(len(queue)):
                print(queue)

                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    

                    if nr < 0 or nc < 0 or nc >= COLS or nr >= ROWS or grid[nr][nc] in [0, 2]:
                        continue

                    # print(nr, nc)
                    queue.append((nr, nc))
                    grid[nr][nc] = 2

                    fresh_orange -= 1
                    print(f'{fresh_orange=}')
            res += 1

        

        return res if fresh_orange == 0 else -1
