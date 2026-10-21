class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        def recursive_search(r,c):
            if grid[r][c] == "0":
                return
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            
            if grid[r][c] == "1":
                grid[r][c] = "0"
                recursive_search(r, c -1)
                recursive_search(r, c +1 )
                recursive_search(r-1, c)
                recursive_search(r + 1, c)
            
            
            islands = 0

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == "1":
                        islands += 1
                        recursive_search(r, c)
        return islands

                

            



            