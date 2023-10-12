class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(4 - sum(grid[i + dx][j + dy] if i + dx < len(grid) and j + dy < len(grid[0]) else 0 for dx, dy in [(0, 1), (1, 0)]) * 2 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1)
