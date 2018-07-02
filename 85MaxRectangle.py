class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
        	return 0
        #generate column accumulation
        m = len(matrix)+1
        n = len(matrix[0]) + 1
        a = [[0]*n for _ in range(m)]
        b = [[0]*n for _ in range(m)]
        c = [[0]*n for _ in range(m)]
        #scan matrix by row and saved in a:
        #scan matrix by column and saved in b:
        for i in range(1, m):
        	for j in range(1, n):
        		if matrix[i-1][j-1] == '1':
        			a[i][j] = a[i-1][j] + 1
        			b[i][j] = b[i][j-1] + 1
        for i in range(1, m):
        	for j in range(1, n):
        		if a[i][j] < 2 or b[i][j] < 2:#single row/column rect
        			c[i][j] = a[i][j]*b[i][j]
        		else:
        			temp1 = []
        			temp2 = []
        			for x in range(b[i][j]-1):
        				temp1.append((b[i][j]-x)*min(a[i][y] for y in range(j-b[i][j]+x+1,j+1)))
        			for y in range(a[i][j]-1):
        				temp2.append((a[i][j]-y)*min(b[x][j] for x in range(i-a[i][j]+y+1,i+1)))
        			# print(temp1, temp2)
        			c[i][j] = max(max(temp1), max(temp2))
        result = map(max, c)
        return max(result)





def main():
	matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

	# matrix = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
	# matrix = [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]
	foo = Solution()
	print(foo.maximalRectangle(matrix))

if __name__ == '__main__':
	main()


