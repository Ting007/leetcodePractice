class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
        	for j in range(i):
        		dp[i] += ['('+x+')' + y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]

        

def main():
	foo = Solution()
	x = foo.generateParenthesis(3)
	print(x)

if __name__ == '__main__':
	main()



"""
To generate all n-pair parentheses, we can do the following:

Generate one pair: ()

Generate 0 pair inside, n - 1 afterward: () (...)...

Generate 1 pair inside, n - 2 afterward: (()) (...)...

...

Generate n - 1 pair inside, 0 afterward: ((...))
dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp


"""

        	

