class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
        	return ''
        shortest = len(strs[0])
        for words in strs:
        	shortest = min(shortest, len(words))
        common = strs[0][:shortest]
        # for j in range(shortest):
        for w in strs:
        	if len(common)> 0 and common != w[:len(common)]:
        		common = common[:-1]
        		continue
        return common
        


def main():
	s = ["flower","flow","flight"]
	# s = []
    s = ["flower","flow","flight"]
	foo = Solution()
	foo.longestCommonPrefix(s)

if __name__ == '__main__':
	main()