class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        # simple method by others
		total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total
        """
        if not prices:
            return 0
        profit = 0
        i = 0
        buy = prices[i]
        while i < len(prices)-1:
            while i < len(prices)-2 and prices[i+1]<prices[i]:
                i = i +1
            j = i+1
            while j < len(prices)-1 and prices[j+1] > prices[j]:
                j = j+1
            if (prices[j]-prices[i]) > 0:
                profit += (prices[j]-prices[i])
            i = j+1
        return profit

def main():
	s = [3,3,5,0,0,3,1,4] #5
	# s = [5,4,3,2,1] #0
	s = [1,2,3,4,5]
	# s = [2,1,2,0,1] #1
	# s = [2,0,1,7,0,8,3] #5
	# s = [3,2,6,5,0,3]
	foo = Solution()
	a = foo.maxProfit(s)
	print(a)

if __name__ == '__main__':
	main()

