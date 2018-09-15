class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        subs = s.split()
        print(subs)
        for i in range(len(subs)):
        	subs[i] = subs[i][::-1]
        return " ".join(subs)

if __name__ == '__main__':
	s = "s'teL ekat edoCteeL tsetnoc"
	foo = Solution()
	x = foo.reverseWords(s)
	print(x)
