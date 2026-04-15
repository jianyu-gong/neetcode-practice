class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        chest_queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    chest_queue.append((r,c))

        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # print(chest_queue)
        
        while chest_queue:
            level = 1
            VISITED = set()
            r, c = chest_queue.pop()
            
            temp_queue = [(r, c)]
            # print(temp_queue)

            while temp_queue:
                for i in range(len(temp_queue)):
                    row, col = temp_queue.pop(0)
                    # print(f'{row=}, {col=}')

                    for dr, dc in DIRECTIONS:
                        # print(f'{dr=}, {dc=}')
                        ndr, ndc = dr + row, dc + col
                        

                        if ndr < 0 or ndc < 0 or ndr >= ROWS or ndc >= COLS or (ndr, ndc) in VISITED or grid[ndr][ndc] <= 0:
                            continue

                        # print(f'{ndr=}, {ndc=}, {level=}, val={grid[ndr][ndc]}')

                        grid[ndr][ndc] = min(level, grid[ndr][ndc])
                        VISITED.add((ndr, ndc))
                        temp_queue.append((ndr, ndc))

                        # print(grid)
                    # print(len(temp_queue))

                level += 1

        # print(grid)

#  (0, 0) (0, 1) (0, 2) (0, 3)
#  (1, 0) (1, 1) (1, 2) (1, 3)
#  (2, 0) (2, 1) (2, 2) (2, 3)
#. (3, 0) (3, 1) (3, 2) (3, 3)
#
#
#
        

            

            


    