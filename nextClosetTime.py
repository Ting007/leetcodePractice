import collections
class Solution:
	def NextTime(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		n = s.split(':')# ['23', '59']
		c = collections.Counter(s)
		digit = list(c)
		digit.sort()
		hour = int(n[0])
		minu = int(n[1])
		while minu < 60:
			minu += 1
			if str(minu)[0] in c and str(minu)[1] in c:
				return str(hour)+':'+str(minu)
		while hour < 24:
			hour += 1
			if str(hour)[0] in c and str(hour)[1] in c:
				minu = str(digit[0]) + str(digit[1])
				return str(hour)+':'+str(minu)
		return str(digit[0])*2 + ':'+ str(digit[0])*2





def main():
	input = ["19:34", "14:59", "09:30", "23:05", "23:58"] # 19:39 15:14 09:33 23:20 22:22
	foo = Solution()
	for s in input:
		x = foo.NextTime(s)
		print(x)

if __name__ == '__main__':
	main()