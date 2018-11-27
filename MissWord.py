class Solution:
	def missWords(self, t1, t2):
		"""
        :type input: str
        :rtype: int
		"""
		res = []
		pStr = t1.split(" ")
		subStr = t2.split(" ")
		j = 0
		for i in range(len(pStr)):
			if j < len(subStr) and pStr[i] == subStr[j]:
				j += 1
			else:
				res.append(pStr[i])
		return res

if __name__ == '__main__':
	foo = Solution()
	x = foo.missWords("I like eating cheese", "I cheese")
	print(x)


