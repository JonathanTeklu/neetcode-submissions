from collections import deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = deque([(0,0,1)])  #queue start at first index with val of 1 beecause its valid
        grid[0][0] = 1 #mark first one as visited
        
        directions = [ (-1,-1), (-1,0), (-1,1),
                    (0,-1), (0,1),

                    (1,-1), (1,0), (1,1)
         ]

        while queue: 
            row, col, length = queue.popleft()

            if row == n-1 and col == n- 1:
                return length
            

            for rowchange, colchange in directions:    
                newcol = col + colchange
                newrow = row + rowchange
            if 0 <= newrow < n and 0 <= newcol < n and grid[newrow][newcol] == 0:
                
                grid[newrow][newcol] =  1

                queue.append((newrow, newcol, length + 1))

        return -1 

