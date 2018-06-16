import math
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        x_len = int(math.log10(x))+1
        origin = x
        rev = 0
        for i in range(x_len):
        	remainder = x%10
        	x = int(x/10)
        	rev = rev*10 + remainder
        	#print(rev, remainder)
        if rev == origin:
        	return True

        return False



def main():
	foo = Solution()
	sample = [121, 2442, 111, 31913, 124421]
	for s in sample:
		print(foo.isPalindrome(s))

if __name__ == '__main__':
	main()