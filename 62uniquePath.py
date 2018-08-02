class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #generate the 2d matrix for the grid
        dp = [[0]*n for _ in range(m)]
        #initial the staring point
        dp[0][0] = 1

        #set the first column as 1
        for i in range(1, m):
        	dp[i][0] = dp[i-1][0]
        #set the first row as 1
        for i in range(1, n):
        	dp[0][i] = dp[0][i-1]

        # start calculate the grid
        for i in range(1, m):
        	for j in range(1, n):
        		dp[i][j] = dp[i-1][j] + dp[i][j-1]
        		
        return dp[m-1][n-1]