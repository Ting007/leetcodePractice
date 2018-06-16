class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        seq = str(x)
        half = int(len(seq)/2)+1
        for i in range(half):
        	if seq[i] != seq[len(seq)-i-1]:
        		return False
        return True



def main():
	foo = Solution()
	sample = [121, 2442, 111, 31913, 124421]
	for s in sample:
		print(foo.isPalindrome(s))

if __name__ == '__main__':
	main()