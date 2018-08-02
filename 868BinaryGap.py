class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        counter = 0 #initialize the counter for the zeros
        #calculate the inital quotient and mod of N/2
        quotient, modulo = divmod(N, 2)
        #iterate N, until reach the first mod of one
        while modulo == 0:
        	quotient, modulo = divmod(quotient, 2)
        #Keep dividing, find out the next '1'#
        #calculate the distance between the first 1 and second 1
        while quotient > 0:
        	quotient, modulo = divmod(quotient, 2)
        	temp = 0
        	while modulo == 0:
        		temp += 1
        		quotient, modulo = divmod(quotient, 2)
        	counter = max(counter, temp+1)
        	temp = 0 # reset the temp counter to 0, when reach 1 as a remainder
        return counter

def main():
	foo = Solution()
	s = [22, 5, 6, 8]
	for i in s:
		x = foo.binaryGap(i)
		print(x)

if __name__ == '__main__':
	main()
