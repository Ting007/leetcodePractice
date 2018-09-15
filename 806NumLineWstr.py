import unittest
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        helper = "abcdefghijklmnopqrstuvwxyz"
        res_len, line = 0, 0
        for char in S:
        	i = helper.find(char)
        	temp = widths[i] + res_len
        	if temp <= 100:
        		res_len = temp
        	else:
        		res_len = widths[i]
        		line += 1
        if line > 0 or res_len > 0:
        	line += 1
        return [line, res_len]

class TestSolution(unittest.TestCase):
	def test1(self):
		widths =[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
		S = "abcdefghijklmnopqrstuvwxyz"
		foo = Solution()
		self.assertEqual(foo.numberOfLines(widths, S), [3, 60])

	def test2(self):
		widths =[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
		S = "bbbdddcccaaa"
		foo = Solution()
		self.assertEqual(foo.numberOfLines(widths, S), [2, 4])

	def test3(self):
		widths =[0,0,0,0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
		S = "bbbdddcccaaa"
		foo = Solution()
		self.assertEqual(foo.numberOfLines(widths, S), [0, 0])

	def test4(self):
		widths =[0,0,10,0,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
		S = "bbbdddcccaaa"
		foo = Solution()
		self.assertEqual(foo.numberOfLines(widths, S), [1, 30])



if __name__ == '__main__':
	unittest.main()
	