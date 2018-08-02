class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        #score used to store the score for each row of A
        score = [] 
        # flip the rows of A if there are leading zeros
        for x in A:
            if x[0] == 0:
                self.zeroToOne(x)
        # transpose A, rows into columns
        A = [list(x) for x in zip(*A)]
        # flip the matrix
        self.flipMatrix(A)
        # transpose A back to the original
        A = [list(x) for x in zip(*A)]
        #calculate score of each row of A
        for row in A:
        	score.append(self.score(row))
        return sum(score)


    def flipMatrix(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        flip the matrix by checking if there are more 0 in each row or column
        """
        for x in range(1, len(A)):
            ones = A[x].count(1)
            zeros = A[x].count(0)
            # flip 1 and 0 but avoid fliping the leading zeros.
            if zeros >= ones:
                self.zeroToOne(A[x])

    def zeroToOne(self, x):
    	"""
    	:tyep x: List[int]
    	:rtype: None
    	convert all the 1 into 0 and 0 into 1
    	"""
    	for i in range(len(x)):
    		if x[i] == 0:
    			x[i] = 1
    		else:
    			x[i] = 0

    def score(self, x):
    	"""
    	:type x: list[int]
    	:rtype: int
    	calculate the dec number of binary meaning of each row of A
    	"""
    	binary = ''
    	for i in x:
    		binary += str(i)
    	return int(binary, 2)

def main():
	A1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]] #39
	A2 = [[1,0,0],[1,0,1]] #13
	A3 = [[0,1,1],[1,1,1],[0,1,0]] #18
	sample = [A1, A2, A3]
	foo = Solution()
	for A in sample:
		result = foo.matrixScore(A)
		print(result)

if __name__ == '__main__':
	main()