class Solution:
	def longestPalindrome(self, s):
		dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s))]
		index = 0
		longest = 1

		for i in range(0, len(s)):
			for j in range(0, len(s)):
				if s[i] == s[j]:
					dp[i][j] = dp[i-1][j+1]+1
					# in case there could be some words not palindrome
					if dp[i][j] > longest and abs(i-j) <= longest:
						longest = dp[i][j]
						index = j
		return s[index:(index+longest)]



def main():
	# s = "babad"
	# s = "cbbd"
	# s = "abb"
	s = "ccc"
	s = "abcdasycsdfghjkldcba"
	foo = Solution()

	print(foo.longestPalindrome(s))

if __name__ == '__main__':
	main()