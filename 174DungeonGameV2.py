class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        #initialize the matrix to store the treats along the path
        A = [[0]*(n+1) for _ in range(m+1)]
        A[m][n-1] = 1
        A[m-1][n] = 1
        #start from the final point
        for i in range(m-1, -1, -1):
        	for j in range(n-1, -1, -1):
        		if i == m-1:
        			if dungeon[i][j] < A[i][j+1]:
        				A[i][j] = A[i][j+1] - dungeon[i][j]
        			else:
        				A[i][j] = 1

        		elif j == n-1:
        			if dungeon[i][j] < A[i+1][j]:
        				A[i][j] = A[i+1][j] - dungeon[i][j]
        			else:
        				A[i][j] = 1
        		else:
        			if dungeon[i][j] < min(A[i+1][j], A[i][j+1]):
        				A[i][j] = min(A[i+1][j], A[i][j+1]) - dungeon[i][j]
        			else:
        				A[i][j] = 1
        return A[0][0]




       

def main():
	foo = Solution()
	s = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
	s = [[100]]
	s = [[-3, 5]]
	x = foo.calculateMinimumHP(s)
	print(x)

if __name__ == '__main__':
	main()




