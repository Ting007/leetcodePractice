class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        while matrix:
        	res.extend(matrix[0])
        	matrix = [*zip(*matrix)][::-1]
        return res
