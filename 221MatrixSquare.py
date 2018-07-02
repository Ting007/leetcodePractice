class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)+1
        n = len(matrix[0])+1
        a = [[0 for _ in range(n)] for _ in range(m)]
        # print(a)
        for i in range(1, m):
        	for j in range(1, n):
        		if matrix[i-1][j-1] == "1":
        			a[i][j] = min(a[i-1][j-1], min(a[i-1][j], a[i][j-1]))+1
        width = max(a[i][j] for i in range(m) for j in range(n))
        return width*width



def main():
	# matrix=[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
	matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
	foo = Solution()
	print(foo.maximalSquare(matrix))

if __name__ == '__main__':
	main()