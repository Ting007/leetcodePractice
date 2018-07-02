class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
        	return ""

        common = ""
        for i, a in enumerate(zip(*strs)):
        	if len(set(a)) == 1:
        		common += strs[0][i]
        	else:
        		break
        return common

def main():
	foo = Solution()
	s = ["flower","flow","flight"]
	print(foo.longestCommonPrefix(s))

if __name__ == '__main__':
	main()