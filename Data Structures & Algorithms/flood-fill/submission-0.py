class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        row, col = len(image), len(image[0])
        org = image[sr][sc]

        def dfs(r, c, visited):
            if min(r, c) < 0 or r == row or c  == col or (r, c) in visited or image[r][c] != org:
                return

            if image[r][c] == org:
                image[r][c] = color

            visited.add((r,c))

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

            visited.remove((r,c))


        dfs(sr, sc, visited)

        return image