class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)//+1):
            # print(i, s[:i])
            if len(s)%i== 0:
                if s == s[:i]*(len(s)//i):
                    return True
        return False

if __name__ == '__main__':
	foo = Solution()
	sample = ["abab", "aba", "abcabcabcabcabc", "aabaaba"]
	for s in sample:
		x = foo.repeatedSubstringPattern(s)
		print(x)