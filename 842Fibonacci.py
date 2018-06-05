class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        splice = []
        i = len(S)
        max_len = int(i/2)
        for m in range(1, max_len+1):
        	num1 = S[:m]
        	num2_right = int(m+1+(i-m)/2)
        	for n in range(m+1, num2_right):
        		num2 = S[m:n]
        		if self.compare(S, num1, num2, splice):
        			return splice
        		else:
        			splice = []
        return []
        		
    def compare(self, num, num1, num2, splice):
    	if (num1[0] =='0' and len(num1) > 1) or (num2[0] == '0' and len(num2)>1):
    		return False
    	limit = 2**31-1
    	addition = int(num1)+int(num2)
    	if (int(num1)> limit or int(num2) > limit or addition > limit):
    		return False 
    	total = str(addition)
    	shift = len(total)
    	point = len(num1) + len(num2)
    	sum_right = point+shift
    	expected = num[point:sum_right]
    	# print(num, num1, num2, expected)
    	# print(splice)
    	if expected == total:
    		splice.append(int(num1))
    		if sum_right == len(num):
    			splice.append(int(num2))
    			splice.append(int(total))
    			return True
	    	if self.compare(num[len(num1):], num2, total, splice):
	    		return True
    	return False


def main():
	foo = Solution()
	S = ["1123581321", "123456579", "112358130", "0123", "1101111"]
	for s in S:
		print(foo.splitIntoFibonacci(s))

	s = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
	print(foo.splitIntoFibonacci(s))

	s = "3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909"
	print(foo.splitIntoFibonacci(s))
if __name__ == '__main__':
	main()



