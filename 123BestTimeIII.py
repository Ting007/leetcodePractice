class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
        	return 0
        buy1 = float('-inf')
        buy2 = float('-inf')
        sell1 = 0
        sell2 = 0
        # this algorithm is calculate the balance on your account
        #each buy and sell, try to maximaze the balance
        for p in prices:
            buy1 = max(buy1, -p) # after buy the stock, the balance is negative.
            sell1 = max(sell1, p+buy1)#after the selling, profit 
            buy2 = max(buy2, sell1-p) # after the second by
            sell2 = max(sell2, buy2+p) # affter selling the second
            # print(buy1, sell1, buy2, sell2)
        return sell2


def main():
	# s = [3,3,5,0,0,3,1,4] #5
	# s = [5,4,3,2,1] #0
	# s = [1,2,3,4,5]
	s = [2,1,2,0,1] #1
	# s = [2,0,1,7,0,8,3] #5
	# s = [1,2,4,2,5,7,2,4,9,0]
	foo = Solution()
	a = foo.maxProfit(s)
	print(a)

if __name__ == '__main__':
	main()

