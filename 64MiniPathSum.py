import unittest
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in range(len(grid)):
            for j in range(len(grid[0])):
            	if i == 0 and j > 0:
            		grid[i][j] = grid[i][j] + grid[i][j-1]
            	elif j == 0 and i > 0:
            		grid[i][j] = grid[i][j] + grid[i-1][j]
            	elif i > 0 and j > 0:
            		grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]


class TestSolution(unittest.TestCase):
	def test1(self):
		grid = [[1,3,1], [1,5,1], [4,2,1]]
		foo = Solution()
		self.assertEqual(foo.minPathSum(grid), 7)

if __name__ == '__main__':
	unittest.main()