class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s[0]
        temp = ""
        if len(set(s)) < 2:
        	return s
        else:
        	for x in range(len(s)):
        		i = x
        		j = len(s)-1
        		while i < j:
        			if s[i] == s[j] and j-i > len(result)-1:
        				if self.isPalindrome(s[i+1:j]):
        					temp = s[i:(j+1)]
        					if len(temp) > len(result):
        						result = temp
        			j -=1
        		
        return result
        		


    def isPalindrome(self, s):
        if len(s) < 2:
        	return True
        if s[0] == s[-1]:
        	return self.isPalindrome(s[1:(-1)])
        else:
        	return False

def main():
        foo = Solution()
        s="ohomm"
        print(foo.longestPalindrome(s))
        s= "asjrgapajk"
        print(foo.longestPalindrome(s))
        s="babad"
        print(foo.longestPalindrome(s))
        s="cbbc"
        print(foo.longestPalindrome(s))
        s="acccb"
        print(foo.longestPalindrome(s))
        s="aaaa"
        print(foo.longestPalindrome(s))
        s="abcda"
        print(foo.longestPalindrome(s))
        s="bananas"
        print(foo.longestPalindrome(s))
        s="aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
        print(foo.longestPalindrome(s))
        s="aaabaaaa"
        print(foo.longestPalindrome(s))
        s = "babadada"
        print(foo.longestPalindrome(s))

if __name__ == "__main__":
	main()

        



