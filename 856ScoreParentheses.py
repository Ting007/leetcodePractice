class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S == "":
        	return 0
        if S == "()":
        	return 1
        score = 0
        if S[0] == '(' and S[1] == '(':
        	i = self.findSplit(S)
        	temp1 = S[1:i]
        	temp2 = S[(i+1):]
        	score = 2*(self.scoreOfParentheses(temp1)) + self.scoreOfParentheses(temp2)
        if S[0] == '(' and S[1] == ')':
        	temp = S[2:]
        	score = 1 + self.scoreOfParentheses(temp)
        return score

    def findSplit(self, S):
    	"""
		:type: str
		:rtype: int
		for example:
			S = '(())()'
			return 3
    	"""
    	stack = []
    	for i in range(len(S)):
    		if S[i] == '(':
    			stack.append(S[i])
    		if S[i] == ')':
    			stack.pop()
    		if stack == []:
    			return i
    	return i


def main():
	foo = Solution()
	s = ["()", '(())', '()()', '(()(()))', '(())()']
	for i in s:
		x = foo.scoreOfParentheses(i)
		print(x)

if __name__ == '__main__':
	main()