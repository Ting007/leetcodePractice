class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #generate the 2d matrix for the grid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        #initial the staring point
        if obstacleGrid[0][0] == 0:
        	dp[0][0] = 1

        #set the first column as 1
        for i in range(1, m):
        	if obstacleGrid[i][0] == 0:
        		dp[i][0] = dp[i-1][0]
        #set the first row as 1
        for i in range(1, n):
        	if obstacleGrid[0][i] == 0:
        		dp[0][i] = dp[0][i-1]

        # start calculate the grid
        for i in range(1, m):
        	for j in range(1, n):
        		if obstacleGrid[i][j] == 0:
        			dp[i][j] = dp[i-1][j] + dp[i][j-1]
        		else:
        			dp[i][j] = 0
        return dp[m-1][n-1]




def main():
	grid = [[0,0,0], [0,1,0],[0,0,0]]
	foo = Solution()
	x = foo.uniquePathsWithObstacles(grid)
	print(x)

if __name__ == '__main__':
	main()