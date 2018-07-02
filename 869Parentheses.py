class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == '()':
        	return 1
        stack = []
        score = 0
        for i in S:
        	if i == '(':
        		stack.append(i)
        	if i == ')':
        		stack.pop()
        		if stack == []:
        			score += 1
        		else:
        			print(score)
        			return self.scoreOfParentheses(S[1:-1])*2
        return score



def main():
	s = ['()','()()','(())', '(()(()))', '(())(())']
	foo = Solution()
	for S in s:
		print(foo.scoreOfParentheses(S))

if __name__ == '__main__':
	main()




