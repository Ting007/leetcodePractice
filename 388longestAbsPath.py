class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        #sparse the string into list of the strings
        total_path = input.split("\n")
        # path = []#save all the length
        pathL = 0
        print(total_path)
        #backtrack of each file from bottom to top level of filepath
        # total_path = ['dir', '\tsubdir1', '\tsubdir2', '\t\tfile.ext']
        for i in range(len(total_path)-1, -1, -1):
        	#search for the files
        	pathlength = 0
        	path = []
        	if total_path[i].find('.') > -1:
        		path.append(total_path[i])
        		# count the number of '/t'
        		for j in range(i-1, -1, -1):
        			if total_path[j].count('\t') == path[-1].count('\t') - 1:
        				path.append(total_path[j])
        				# print(path)
        		for file in path:
        			pathlength += len(file)-file.count('\t') + 1
        		pathL = max(pathL, pathlength-1)
        	print(path)
        	
        return pathL




        		


        return max(path_length)


if __name__ == '__main__':
	s = ["dir\n\t        file.txt\n\tfile2.txt", "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", "a.txt", 'a']
	foo = Solution()
	for i in s:
		x = foo.lengthLongestPath(i)
		print(x)


