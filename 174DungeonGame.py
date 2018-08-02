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
        #start from the final point
        A[m][n-1] = 1
        A[m-1][n] = 1
        # for x in A:
        #   print(x)
        for i in range(m-1, -1, -1):
          if dungeon[i][n-1] >= A[i+1][n-1]:
            A[i][n-1] = 1
          else:
            A[i][n-1] = A[i+1][n-1]-dungeon[i][n-1]
        for i in range(n-1, -1, -1):
          if dungeon[m-1][i] >= A[m-1][i+1]:
            A[m-1][i] = 1
          else:
            A[m-1][i] = A[m-1][i+1]-dungeon[m-1][i]
        
        # for x in A:
        #   print(x)

        for i in range(m-2, -1, -1):
          for j in range(n-2, -1, -1):
            if dungeon[i][j] > 0 and dungeon[i][j] >= min(A[i+1][j], A[i][j+1]):
              A[i][j] = 1
            else:# dungeon[i][j] >= 0:
              A[i][j] = min(A[i+1][j], A[i][j+1]) - dungeon[i][j]

        # for x in A:
        #   print(x)    
       
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




