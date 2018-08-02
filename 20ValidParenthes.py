class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {"(":")", "{":"}", "[":"]"}
        for i in s:
        	if i in brackets.keys():
        		stack.append(brackets[i])
        	if i in brackets.values():
        		if stack == [] or i != stack.pop():
        			return False
        return stack == []

def main():
	foo = Solution()
	s = ["()", "[](){}", "{]", "([)]", "{[]}", "([]"]
	for i in s:
		print(foo.isValid(i))

if __name__ == '__main__':
	main()
