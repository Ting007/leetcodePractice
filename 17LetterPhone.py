class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
        	return []
        comb = {'2':['a', 'b', 'c'],\
        '3':['d', 'e', 'f'],\
        '4':['g','h','i'],\
        '5':['j', 'k', 'l'],\
        '6':['m', 'n', 'o'],\
        '7':['p', 'q', 'r', 's'],\
        '8':['t', 'u', 'v'],\
        '9':['w', 'x', 'y', 'z']}

        if len(digits) == 1:
        	return comb[digits]
        if len(digits) == 2:
        	return self.combinations(comb[digits[0]], comb[digits[1]])
        else:
        	first = digits[:2]
        	partI = self.letterCombinations(first)
        	for i in digits[2:]:
        		partI = self.combinations(partI, comb[i])
        	return partI



    def combinations(self, letters1, letters2):
    	"""
    	:type letters: List[str]
    	['a', 'b', 'c'],
        ['d', 'e', 'f'],
    	:rtype: List[str]
    	["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    	"""
    	m = len(letters1)
    	n = len(letters2)
    	combine = [letters1[i]+letters2[j] for i in range(m) for j in range(n)]
    	return combine

def main():
	foo = Solution()
	s = ["234"]
	for i in s:
		print(foo.letterCombinations(i))

if __name__ == '__main__':
	main()