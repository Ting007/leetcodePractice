class Solution:
    def lengthOfLongestSubstring(self, s):
    	strpair = {}
    	length = []
    	pointer = 0
    	for i in range(len(s)):
    		if s[i] in strpair:
    			if strpair[s[i]][0] >= pointer:
    				dist2 = i - pointer 
	    			pointer = strpair[s[i]][0]+1
	    			dist1 = i - strpair[s[i]][0]
	    			strpair[s[i]][0]=i
	    			length.append(dist1)
	    			length.append(dist2)
	    		else:
	    			strpair[s[i]][0] = i
    		else:
    			strpair[s[i]]=[i]
    			if pointer == 0:
    				length.append(i+1)

    	# for key, value in strpair.items():
    	# 	print(key, value)
    	dist = len(s) - pointer
    	length.append(dist)
    	if len(length) == 0:
    		return len(s)
    	return (max(length))
def main():
        foo = Solution()
        s="ohomm"
        print(foo.lengthOfLongestSubstring(s))
        s= "asjrgapa"
        print(foo.lengthOfLongestSubstring(s))

if __name__ == "__main__":
        main()