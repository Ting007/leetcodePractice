class Solution:
    def compare(self, s, n):
    	"""
    	:type s:str
    	:type i:int
    	:rtype str
    	"""
    	
    	if (n[0] <= 0 or (n[1]+1) >= len(s)) and s[n[0]] != s[n[1]]:
    		n[0] +=1
    		n[1] -=1
    		return
    	elif s[n[0]] != s[n[1]]:
    		n[0] +=1
    		n[1] -=1
    		return
    	elif (n[0] <= 0 or (n[1]+1) >= len(s)) and s[n[0]] == s[n[1]]:
    		return
    	elif s[n[0]] == s[n[1]]:
    		n[0] -= 1
    		n[1] += 1
    		return self.compare(s, n)
    	
		

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1:
        	return s
        center1 = [[0, 0]] #save the edges of palindrome
        i = 0
        plndrm = s[0]
        while i < len(s)-1:
        	
        	if s[i] == s[i+1]:
        		if s[i] == s[i-1]:
        			if i+1 < len(s)-1:
        				center1[-1] = [center1[-1][0], i+1]
        				i+=1
        			else:
        				center1[-1] = [center1[-1][0], len(s)-1]
        				i+=2
        		else:
        			center1.append([i, i+1])
        			i += 1
        	elif i > 0 and s[i-1] == s[i+1]:
        		if s[i] == s[i-1]:
        			center1[-1]=[center1[-1][0], i+1]
        			i+=2
        		else:
        			center1.append([i-1, i+1])
        			i += 1
        	else:
        		i += 1
        #print(*center1)
        for n in  center1:
        	# n[0] is the left edge, n[1] is the right edge 
        	self.compare(s,n)
        	dist = n[1] - n[0] +1 # abba dist = 4, bb dist = 2 
        	if dist > len(plndrm):
        		plndrm = s[n[0]:(n[1]+1)]

        return plndrm

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

if __name__ == "__main__":
	main()