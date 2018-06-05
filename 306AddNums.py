class Solution:
	def isAdditiveNumber(self, num):
		"""
		:type num:str
		:rtype: bool
		"""
		i = len(num) # i is the length of the num
		if i < 3:
			return False
		maxi_len = int(i/2) # the possible digit of each num
		for m in range(1, maxi_len+1):
			end = int(m+1+(i-m)/2)
			for n in range(m+1, end+1):
				num1 = num[:m]
				num2 = num[m:n]
				if self.compare(num, num1, num2):
					return True
		return False


	def compare(self, num, num1, num2):
		if (num1[0] == '0' and len(num1) > 1) or (num2[0] == '0' and len(num2) > 1):
			return False
		total = str(int(num1) + int(num2))
		shift = len(total)
		start = len(num1)+len(num2)
		expected = num[start:start+shift]
		#print(num1, num2, expected)
		if total == expected:
			if start+shift >= len(num):
				return True
			num = num[len(num1):]
			#Here is very tricky, you should know that num2 become num1, total is the next num1
			return self.compare(num, num2, total)
		return False

		


def main():
        foo = Solution()
        # s = "112358" #True
        # print(foo.isAdditiveNumber(s))
        # s = "199100199" #True
        # print(foo.isAdditiveNumber(s))
        # s = "101020305080130210" #True
        # print(foo.isAdditiveNumber(s))
        # s = "1023" #False
        # print(foo.isAdditiveNumber(s))
        s = "000" #True
        print(foo.isAdditiveNumber(s))
        s = "8917" #True
        print(foo.isAdditiveNumber(s))
        s = "1203" #False
        print(foo.isAdditiveNumber(s))
        s = "0235813" #False
        print(foo.isAdditiveNumber(s))
        s = "199001200" #False
        print(foo.isAdditiveNumber(s))
        s = "12012122436" #True
        print(foo.isAdditiveNumber(s))

if __name__ == "__main__":
	main()