class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
        	if prices[i] < prices[i+1]:
        		sell = max(prices[(i+1):])
        		profit = max(profit, sell-prices[i])
        return profit

def main():
	s = [7,1,5,3,6,4] #5
	# s = [5,4,3,2,1] #0
	# s = [2,1,2,0,1] #1
	# s = [2,0,1,7,0,8,3] #5
	s = [3,2,6,5,0,3]
	foo = Solution()
	a = foo.maxProfit(s)
	print(a)

if __name__ == '__main__':
	main()
