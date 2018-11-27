import collections
import re

class Solution:
	def hostNum(self, infile):
		f = open(infile, 'r')
		dis = f.readlines()
		f.close
		hostCount = collections.defaultdict(int)
		for line in dis:
			host = re.split(' ', line)
			hostCount[host[0]] += 1
		with open("output_host.txt",'w') as file:
			for key, value in hostCount.items():
				file.write(key+' '+str(value))

if __name__ == '__main__':
	foo = Solution()
	foo.hostNum("input_host_access.txt")




		